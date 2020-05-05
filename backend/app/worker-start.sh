#! /usr/bin/env bash
set -e

python /app/app/celeryworker_pre_start.py

celery worker -A app.worker -B -l info -c 1
