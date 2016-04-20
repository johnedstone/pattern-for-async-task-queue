#!/bin/sh
sleep 10
su -m myuser -c "gunicorn --access-logfile - --bind=0.0.0.0:5000 server:app"
# flask -a server:app --debug run
