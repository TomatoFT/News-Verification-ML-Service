#!/bin/bash

# Redirect cron logs to stdout
touch /var/log/cron.log
ln -sf /dev/stdout /var/log/cron.log

# Schedule your cron job (every day at 2 AM)
echo "0 2 * * * /usr/local/bin/python /app/your_script.py" | crontab -

# Start cron in the foreground
cron && tail -f /var/log/cron.log
