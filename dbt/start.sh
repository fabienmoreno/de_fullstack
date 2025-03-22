#!/bin/bash

# Start cron in background
service cron start

# Ensure the dbt log file exists
touch /var/log/cron/dbt.log

# Keep the container running by tailing the log
tail -F /var/log/cron/dbt.log
