@ECHO OFF
cd ..
docker pull marianadmoreira/tema11
docker run --name tema11c marianadmoreira/tema11
docker cp tema11c:\tema11\finalResults\ ..\Docker-ELK\logstash\files\
docker stop tema11c