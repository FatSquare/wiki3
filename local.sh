#! /usr/bin/bash

git pull
source env/bin/activate;
rm -rf wiki/static/*
python wiki/manage.py collectstatic 
python wiki/manage.py runserver 
