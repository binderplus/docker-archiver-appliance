#!/usr/bin/env python

# This script adds a EPICS archiver appliance MySQL connection pool to a Tomcat context.xml
# The location of context.xml is determined by the ${CATALINA_HOME} environment variable
# The parameters for the connection pool are determined by the ${MYSQL_HOST}, 
# ${MYSQL_DATABASE}, ${MYSQL_USER} and ${MYSQL_PASSWORD} environment variables.
try:
    import sys
    import os
    import xml.dom.minidom

    mysql_host = os.getenv('MYSQL_HOST')
    if not mysql_host:
        print 'The environment variable MYSQL_HOST is not defined. Assuming localhost'
        mysql_host = 'localhost'

    mysql_database = os.getenv('MYSQL_DATABASE')
    if not mysql_database:
        print 'The environment variable MYSQL_DATABASE is not defined.'
        sys.exit(1)

    mysql_user = os.getenv('MYSQL_USER')
    if not mysql_user:
        print 'The environment variable MYSQL_USER is not defined.'
        sys.exit(1)

    mysql_password = os.getenv('MYSQL_PASSWORD')
    if not mysql_password:
        print 'The environment variable MYSQL_PASSWORD is not defined.'
        sys.exit(1)

    catalina_home = os.getenv("CATALINA_HOME")
    if not catalina_home:
        print "We determine the location of context.xml using the environment variable CATALINA_HOME which does not seem to be set."
        sys.exit(1)

    context_xml = catalina_home + '/conf/context.xml'
    print "Setting MySQL connection parameters in ", context_xml

    context_dom = xml.dom.minidom.parse(context_xml)

    connpool = context_dom.createElement('Resource')
    connpool.setAttribute('name', "jdbc/archappl")
    connpool.setAttribute('auth', "Container")
    connpool.setAttribute('type', "javax.sql.DataSource")
    connpool.setAttribute(
        'factory', "org.apache.tomcat.jdbc.pool.DataSourceFactory")
    connpool.setAttribute('testWhileIdle', "true")
    connpool.setAttribute('testOnBorrow', "true")
    connpool.setAttribute('testOnReturn', "false")
    connpool.setAttribute('validationQuery', "SELECT 1")
    connpool.setAttribute('validationInterval', "30000")
    connpool.setAttribute('timeBetweenEvictionRunsMillis', "30000")
    connpool.setAttribute('maxActive', "10")
    connpool.setAttribute('minIdle', "2")
    connpool.setAttribute('maxWait', "10000")
    connpool.setAttribute('initialSize', "2")
    connpool.setAttribute('removeAbandonedTimeout', "60")
    connpool.setAttribute('removeAbandoned', "true")
    connpool.setAttribute('logAbandoned', "true")
    connpool.setAttribute('minEvictableIdleTimeMillis', "30000")
    connpool.setAttribute('jmxEnabled', "true")
    connpool.setAttribute('driverClassName', "com.mysql.jdbc.Driver")
    connpool.setAttribute('url', "jdbc:mysql://" +
                            mysql_host + ":3306/" + mysql_database)
    connpool.setAttribute('username', mysql_user)
    connpool.setAttribute('password', mysql_password)

    context_dom.getElementsByTagName('Context')[0].appendChild(connpool)

    with open(context_xml, 'w') as file:
        file.write(context_dom.toprettyxml())

except Exception as err:
    print "ERROR: ", err
