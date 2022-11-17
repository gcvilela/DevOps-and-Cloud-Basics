#!/bin/bash
docker build -t tema10 .
docker container prune -f
