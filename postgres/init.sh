#!/bin/bash
set -e

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" <<-EOSQL
    CREATE DATABASE longrangeiothackathon;
    \\connect longrangeiothackathon;
    CREATE TABLE trashlevel(
      id serial not null,
      timestamp timestamp default current_timestamp,
      level integer
    );
EOSQL
