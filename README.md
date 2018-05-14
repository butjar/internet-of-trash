Internet-of-trash
=================

Eclipse-Mosquitto
-----------------

Docker
------
https://www.docker.com/#/get\_started
https://docs.docker.com/compose/

```
docker-compose up worker=5
```

Datadog
-------
https://docs.datadoghq.com/integrations/faq/postgres-custom-metric-collection-explained/

Postgres
--------
```
PGPASSWORD=admin psql -h localhost -U admin -d longrangeiothackathon -c "SELECT * FROM trashlevel;"
```

```
psql -U admin -d longrangeiothackathon -h 127.0.0.1
```

Test
----

```
./pub.sh
```

```
./sub.sh
```
