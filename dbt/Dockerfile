FROM ghcr.io/dbt-labs/dbt-postgres:1.9.0

# Install cron
RUN apt-get update && \
    apt-get install -y cron && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /usr/app

# Copy all dbt files to working directory
COPY . /usr/app/

# Explicitly create directory and copy profiles.yml
RUN mkdir -p /root/.dbt
COPY profiles.yml /root/.dbt/profiles.yml

# Install dependencies
RUN dbt deps

# Create log directory
RUN mkdir -p /var/log/cron

# Add cron job to run dbt every 5 minutes
RUN echo "*/5 * * * * cd /app && dbt run >> /var/log/cron/dbt.log 2>&1" > /etc/cron.d/dbt-cron && \
    chmod 0644 /etc/cron.d/dbt-cron && \
    crontab /etc/cron.d/dbt-cron

# Add startup script to run cron and keep container alive
COPY start.sh /start.sh
RUN chmod +x /start.sh

CMD ["/start.sh"]