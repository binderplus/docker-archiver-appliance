#!/usr/bin/env bash

if [ ! -d "${CATALINA_HOME}/webapps/${COMPONENT}" ]
then
    if [ ! -f "${CATALINA_HOME}/webapps/${COMPONENT}.war" ]
    then
        echo "Unable to find ${COMPONENT}.war"
        exit 1
    fi
    
    mkdir ${CATALINA_HOME}/webapps/${COMPONENT}
    pushd ${CATALINA_HOME}/webapps/${COMPONENT}

        echo "Deploying ${COMPONENT}"
        jar xf ${CATALINA_HOME}/webapps/${COMPONENT}.war

    popd
fi

if [ "${COMPONENT}" == "mgmt" ]
then
    if [ -f "${CATALINA_HOME}/archappl_conf/site_specific_content/template_changes.html" ]
    then
        echo "Modifying static content to cater to site specific information"
        java -cp ${CATALINA_HOME}/webapps/mgmt/WEB-INF/classes:${CATALINA_HOME}/webapps/mgmt/WEB-INF/lib/log4j-1.2.17.jar \
        org.epics.archiverappliance.mgmt.bpl.SyncStaticContentHeadersFooters \
        "${CATALINA_HOME}/archappl_conf/site_specific_content/template_changes.html" \
        ${CATALINA_HOME}/webapps/mgmt/ui
    fi

    if [ -d "${CATALINA_HOME}/archappl_conf/site_specific_content/img" ]
    then
        echo "Replacing site specific images"
        cp -R "${CATALINA_HOME}/archappl_conf/site_specific_content/img"/* ${CATALINA_HOME}/webapps/mgmt/ui/comm/img/
    fi
fi