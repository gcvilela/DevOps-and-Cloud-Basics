@ECHO OFF
cd ..
aws s3 sync ..\Docker-ELK\logstash\files\ s3://jt-dataeng-marianadmoreira/tema11/

