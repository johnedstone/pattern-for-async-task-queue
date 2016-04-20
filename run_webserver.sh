#!/bin/sh
sleep 10
su -m myuser -c "gunicorn --bind=0.0.0.0:5000 webserver:app"
