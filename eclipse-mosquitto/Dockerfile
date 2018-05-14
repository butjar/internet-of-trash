FROM eclipse-mosquitto

ADD mosquitto/config/mosquitto.conf /mosquitto/config/mosquitto.conf
ADD etc/mosquitto/passwd /etc/mosquitto/passwd
RUN mosquitto_passwd -U /etc/mosquitto/passwd
