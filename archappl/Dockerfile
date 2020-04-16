FROM tomcat:9-jdk14-openjdk-buster

ENV ARCHAPPL_APPLIANCES=/usr/local/tomcat/archappl_conf/appliances.xml
ENV ARCHAPPL_POLICIES=/usr/local/tomcat/archappl_conf/policies.py
ENV ARCHAPPL_SHORT_TERM_FOLDER=/usr/local/tomcat/storage/sts
ENV ARCHAPPL_MEDIUM_TERM_FOLDER=/usr/local/tomcat/storage/mts
ENV ARCHAPPL_LONG_TERM_FOLDER=/usr/local/tomcat/storage/lts
ENV CATALINA_OPTS="-XX:MaxPermSize=128M -XX:+UseG1GC -Xmx4G -Xms4G -ea"

RUN apt-get update && apt-get install -y netcat

COPY lib/ lib/
COPY bin/ bin/

CMD ["entrypoint.sh"]