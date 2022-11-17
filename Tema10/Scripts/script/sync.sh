#!/bin/bash
WORKSPACE=$1
aws s3 sync "$WORKSPACE/Scripts/finalResults/" "s3://jt-dataeng-marianadmoreira/tema10/finalResults/"

