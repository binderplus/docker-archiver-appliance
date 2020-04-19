#!/usr/bin/env bash

set_server_xml.py
set_context_xml.py
deploy_component.sh

# Use correct version of libraries
ARCH=`uname -m`
if [[ "$ARCH" = 'x86_64' || "$ARCH" = 'amd64' ]]
then
  echo "Using 64 bit versions of libraries"
  export LD_LIBRARY_PATH=${CATALINA_HOME}/webapps/engine/WEB-INF/lib/native/linux-x86_64:${LD_LIBRARY_PATH}
else
  echo "Using 32 bit versions of libraries"
  export LD_LIBRARY_PATH=${CATALINA_HOME}/webapps/engine/WEB-INF/lib/native/linux-x86:${LD_LIBRARY_PATH}
fi

until nc -z -v -w30 localhost 3306
do
    echo "Waiting for database connection..."
    sleep 5
done

cd ${CATALINA_HOME}/logs
catalina.sh run