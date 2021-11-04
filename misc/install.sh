#!/usr/bin/env bash

set -e

echo "Creating virtual python environment"
python3 -m venv venv
source venv/bin/activate

echo "Updating pip"
python3 -m pip install --upgrade pip

echo "Installing python packages"
pip3 install -r requirements.txt

read -n1 -p "Setup the IPAL Transcriber developer tools too? [y,n] " doit
case $doit in  
  y|Y) pwd && pip3 install -r requirements-dev.txt && pre-commit install ;; 
  *) echo "Skipping developer tools" ;; 
esac
