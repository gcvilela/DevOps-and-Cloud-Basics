#!/bin/bash
WORKSPACE=$1
virtualenv tema09-env
source $WORKSPACE/tema09-env/bin/activate
command pip install -r $WORKSPACE/Scripts/requirements.txt
mkdir $WORKSPACE/Scripts/finalResults
mkdir $WORKSPACE/Scripts/imdb/files
