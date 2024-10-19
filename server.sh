#! /usr/bin/bash

git pull
source env/bin/activate;
rm -rf wiki/static/*
python wiki/manage.py collectstatic 
gunicorn -c gunicorn.py wiki.wsgi:application
