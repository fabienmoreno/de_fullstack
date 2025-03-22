#!/bin/bash

echo "[INFO] Starting cron..."
service cron start

echo "[INFO] Tailing dbt log..."
touch /var/log/cron/dbt.log
tail -F /var/log/cron/dbt.log
