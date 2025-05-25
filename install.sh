#!/bin/bash
pkg update -y
pkg install python -y
pkg install git -y
pip install --upgrade pip
pip install -r requirements.txt
