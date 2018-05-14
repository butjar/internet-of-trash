#!/usr/bin/env python

import os
import sys
import configparser
import paho.mqtt.client as mqtt
from rq import Queue
from redis import Redis
from time import sleep
from app.jobs.jobs import storeTrashlevel

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print('Connected with result code {}'.format(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    topic = client.config.get('MQTT','UPLINK_TOPIC')
    client.subscribe(topic)
    print('Subscribed to topic {}'.format(topic))

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print('On Topic {} received message {} '.format(msg.topic, msg.payload))
   
    try:
        job = client.q.enqueue(storeTrashlevel, msg.payload, client.config)
        print('Enqued worker to store trashlevel: {}'.format(msg.payload))
    except Exception as e:
        sys.stderr.write('Error enqueuing job: {}\n'.format(e))

if __name__ == "__main__":
    DEFAULT_SETTINGS_PATH = '{}/settings.ini'.format(
        os.path.abspath(os.path.join(__file__, os.pardir)))
    config = configparser.SafeConfigParser() 
    
    if len(sys.argv) > 1:
        settings_path = sys.argv[1]
    else:
        settings_path = DEFAULT_SETTINGS_PATH

    config.read(settings_path)
    
    if not config:
        settings_path = DEFAULT_SETTINGS_PATH
        config.read(settings_path)

    
    client = mqtt.Client(client_id=config.get('MQTT', 'CLIENT'))
    client.config = config
    client.on_connect = on_connect
    client.on_message = on_message
    
    client.username_pw_set(client.config.get('MQTT', 'USER'),
        password=client.config.get('MQTT', 'PASSWORD'))
    if client.config.has_option('MQTT', 'CA_CERTS'):
        ca_certs_path = client.config.get('MQTT', 'CA_CERTS')
        print('Reading ca certs from: {}'.format(ca_certs_path))
        client.tls_set(ca_certs=ca_certs_path)

    redis_conn = Redis(host=client.config.get('REDIS', 'HOST'))
    q = Queue('mqtt', connection=redis_conn)
    client.q = q

    host = client.config.get('MQTT', 'HOST')
    port = client.config.getint('MQTT', 'PORT')
    keepalive = client.config.getint('MQTT', 'KEEPALIVE')

    connected = False
    connection_timeout = client.config.get('SUBSCRIBER',
        'CONNECTION_TIMEOUT')
    max_retries = client.config.getint('SUBSCRIBER', 'MAX_RETRIES')

    retries = 0
    while not connected:
        try:
            client.connect(host, port, keepalive)
            connected = True
            print('Connected to MQTT server')
        except Exception as e:
            sys.stderr.write(
                'Error while trying to connect to MQTT server: {}\n'.format(e))
            retries += 1
            sleep(float(connection_timeout))
            if retries != 0 and retries >= max_retries:
                raise e
    # Blocking call that processes network traffic, dispatches callbacks and
    # handles reconnecting.
    # Other loop*() functions are available that give a threaded interface and a
    # manual interface.
    client.loop_forever()
