import sys
import os
import json
import time
import psycopg2

def storeTrashlevel(msg, config):
    msg_dict = json.loads(msg)
    pl = msg_dict['payload']
    reordered_payload = ''
    for i in range(len(pl)-1, 0, -2):
        reordered_payload = pl[i-1] + pl[i] + reordered_payload
    trashlevel = int(reordered_payload, 16)
    
    host = config['POSTGRES']['HOST'] 
    user = config['POSTGRES']['USER']
    password = config['POSTGRES']['PASSWORD']
    dbname = config['POSTGRES']['DBNAME']
    conn = psycopg2.connect('host={} dbname={} user={} password={}'.format(
        host, dbname, user, password))
    cur = conn.cursor()
    cur.execute('INSERT INTO trashlevel (level) VALUES (%s);', [trashlevel])
    conn.commit()
    cur.close()
    conn.close()
    return trashlevel
