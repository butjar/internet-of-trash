FROM python:alpine

RUN apk update && \
    apk add --virtual build-deps gcc python-dev musl-dev && \
    apk add postgresql-dev

ADD requirements.txt /app/requirements.txt
WORKDIR /app

RUN pip install -r requirements.txt

ADD setup.py /app/setup.py
ADD app /app/app

RUN python setup.py install
