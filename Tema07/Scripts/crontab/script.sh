#!/bin/bash
source /home/ubuntu/Tema07/TwitterAPI/TwitterAPI-venv/bin/activate
python3 /path/Scripts/main.py
aws s3 sync "/path/Scripts" "s3://path/Scripts/"
