#! /usr/bin/bash

git pull
source env/bin/activate;
python wiki/manage.py collectstatic 
python wiki/manage.py runserver
