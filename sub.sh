#! /bin/bash

DEV_EUI="001bc50670103a31"
FPORT=6
GROUP=24
TOPIC="/sub/v1/users/hackathon-unibo/shared/unibo/apps/2/devices/${DEV_EUI}/uplink/${FPORT}"
HOST="localhost"
USER="hackathon-unibo"
PASSWORD="hackathonembit2018"
PORT=1883
#HOST="ptnetsuite.a2asmartcity.io"
#CA_FILE='./app/app/loranetsuite.crt'
#CLIENT="${USER}::${GROUP}"

mosquitto_sub -u $USER \
        -P $PASSWORD \
        -p $PORT \
        -t $TOPIC \
        -h $HOST \
        -d
#        --cafile ${CA_FILE} \
#        -i $CLIENT \
#        --tls-version tlsv1.2 \
