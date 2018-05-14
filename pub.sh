#! /bin/bash

PAYLOAD="{\"payload\":\"00000046\",\"seqno\":3,\"statistics\":{\"adr\":true,\"channel\":2,\"duplicate\":false,\"freq\":868.5,\"modBW\":125,\"rssi\":-84,\"seqno\":3,\"sf\":12,\"snr\":5.7,\"time\":1526150883374}}"
DEV_EUI="001bc50670103a31"
FPORT=6
TOPIC="/sub/v1/users/hackathon-unibo/shared/unibo/apps/2/devices/${DEV_EUI}/uplink/${FPORT}"
#HOST="ptnetsuite.a2asmartcity.io"
GROUP=24
HOST="localhost"
USER="hackathon-unibo"
PASSWORD="hackathonembit2018"
CLIENT="${USER}::98"
PORT=1883

mosquitto_pub \
        -p $PORT \
        -i $CLIENT \
        -u $USER \
        -P $PASSWORD \
        -t $TOPIC \
        -h $HOST \
        -m $PAYLOAD \
        -d
