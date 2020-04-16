#!/usr/bin/env python

import sys
import os
import xml.dom.minidom
import urlparse

catalina_home = os.getenv('CATALINA_HOME')
if catalina_home == None:
    print 'We determine the source Tomcat distribution using the environment variable CATALINA_HOME which does not seem to be set.'
    sys.exit(1)

this_appliance = os.getenv('ARCHAPPL_MYIDENTITY')
if this_appliance == None:
    print 'We determine the identity of this appliance using the environment variable ARCHAPPL_MYIDENTITY which does not seem to be set.'
    sys.exit(1)

appliances_xml = os.getenv('ARCHAPPL_APPLIANCES')
if appliances_xml == None:
    print 'We determine the location of the appliances.xml file using the environment variable ARCHAPPL_APPLIANCES which does not seem to be set.'
    sys.exit(1)

component = os.getenv('COMPONENT')
if component == None:
    print 'We determine the appliance component in this container using the environment variable APP which does not seem to be set.'
    sys.exit(1)

appliances_dom = xml.dom.minidom.parse(appliances_xml)
appliances = appliances_dom.getElementsByTagName('appliance')
listener_port = ''
for appliance in appliances:
    identity = appliance.getElementsByTagName(
        'identity').item(0).firstChild.data
    if identity != this_appliance:
        continue
    
    listener_url = appliance.getElementsByTagName(
        component + '_url').item(0).firstChild.data
    
    listener_port = str(urlparse.urlparse(listener_url).port)

if listener_port == '':
    raise AssertionError('We have not been able to find this components listener port in appliances.xml.')
    sys.exit(1)

start_stop_ports = {
    'mgmt': '16001',
    'engine': '16002',
    'etl': '16003',
    'retrieval': '16004'
}

server_xml = catalina_home + '/conf/server.xml'
print 'Setting properties for ', component, ' in ', server_xml

server_dom = xml.dom.minidom.parse(server_xml)
server_dom.getElementsByTagName('Server').item(
    0).setAttribute('port', start_stop_ports[component])

# Find the 'Connector' whose 'protocol' is 'HTTP/1.1'
connector_has_been_set = False
for connector in server_dom.getElementsByTagName('Connector'):
    if connector.hasAttribute('protocol') and connector.getAttribute('protocol') == 'HTTP/1.1':
        connector.setAttribute('port', listener_port)
        connector_has_been_set = True
    else:
        print 'Commenting connector with protocol ', connector.getAttribute('protocol'), '. If you do need this connector, you should un-comment this.'
        comment = connector.ownerDocument.createComment(connector.toxml())
        connector.parentNode.replaceChild(comment, connector)
    
    if connector_has_been_set == False:
        raise AssertionError('We have not set the HTTP listener port.')
        sys.exit(1)

with open(catalina_home + '/conf/server.xml', 'w') as file:
    server_dom.writexml(file)
