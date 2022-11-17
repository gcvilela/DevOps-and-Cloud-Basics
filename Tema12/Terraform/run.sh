#!/bin/bash
export AWS_ACCESS_KEY_ID=
export AWS_SECRET_ACCESS_KEY=
export AWS_REGION=us-east-1
sudo yum update -y
sudo amazon-linux-extras install docker 
sudo systemctl enable docker
sudo systemctl start docker
sudo usermod -a -G docker ec2-user
chown -R ec2-user /home/ec2-user/
cd /home/ec2-user/
aws s3 sync s3://jt-marianadmoreira-terraform/ /home/ec2-user/
docker build -t tema12 .
docker run --name container_tema12 tema12
docker wait container_tema12
docker cp container_tema12:/tema12/finalResults/ /home/ec2-user/
docker stop container_tema12
aws s3 sync /home/ec2-user/finalResults/ s3://jt-dataeng-marianadmoreira/tema12/
