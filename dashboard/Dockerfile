FROM python:alpine
ADD requirements.txt setup.py /dashboard/
ADD dashboard /dashboard/dashboard

WORKDIR /dashboard

RUN python setup.py install; \
    pip install -r requirements.txt
CMD ["python", "./dashboard/dashboard.py"]
