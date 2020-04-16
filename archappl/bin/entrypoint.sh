#!/usr/bin/env bash

set_server_xml.py
set_context_xml.py

until nc -z -v -w30 localhost 3306
do
  echo "Waiting for database connection..."
  sleep 5
done

catalina.sh run