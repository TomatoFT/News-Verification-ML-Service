#!/bin/bash

# Redirect cron logs to stdout
touch /var/log/cron.log
ln -sf /dev/stdout /var/log/cron.log

# Schedule your cron job (every day at 18:20)
echo "00 19 * * * /usr/local/bin/python /app/main.py" | crontab -

# Start cron in the foreground
cron && tail -f /var/log/cron.log
