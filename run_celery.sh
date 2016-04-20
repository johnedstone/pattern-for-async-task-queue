#!/bin/sh
su -m myuser -c "celery worker -A worker:app --loglevel=INFO"

