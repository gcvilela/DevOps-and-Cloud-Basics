#!/bin/bash
WORKSPACE=$1
docker run --name container_tema10 tema10
docker cp container_tema10:/tema10/Scripts/finalResults/ $WORKSPACE/Scripts/finalResults/
docker stop container_tema10
