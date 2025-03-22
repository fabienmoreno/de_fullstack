FROM ghcr.io/dbt-labs/dbt-postgres:1.9.0

WORKDIR /usr/app

# Copy all dbt files to working directory
COPY . /usr/app/

# Explicitly create directory and copy profiles.yml
RUN mkdir -p /root/.dbt
COPY profiles.yml /root/.dbt/profiles.yml

# Install dependencies
RUN dbt deps


# Install cron
RUN apt-get update && \
    apt-get install -y cron && \
    rm -rf /var/lib/apt/lists/*

# Create cron log directory
RUN mkdir -p /var/log/cron

# Add the cron job to run dbt every 5 minutes
RUN echo "*/5 * * * * dbt run >> /var/log/cron/dbt.log 2>&1 \n" > /etc/cron.d/dbt-cron

# Give execution permissions and register cron job
RUN chmod 0644 /etc/cron.d/dbt-cron && \
    crontab /etc/cron.d/dbt-cron

# Create wrapper script to start cron and keep container running
RUN echo '#!/bin/bash\n\
service cron start\n\
touch /var/log/cron/dbt.log\n\
tail -f /var/log/cron/dbt.log' > /start.sh && chmod +x /start.sh


# Run wrapper script
CMD ["/bin/bash", "/start.sh"]