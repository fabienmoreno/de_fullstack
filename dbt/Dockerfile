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

# Create log folder for cron logs
RUN mkdir -p /var/log/cron

# Define the cron job directly via shell
RUN echo "*/5 * * * * cd /app && dbt run >> /var/log/cron/dbt.log 2>&1" > /etc/cron.d/dbt-cron

# Give proper permissions and register the cron job
RUN chmod 0644 /etc/cron.d/dbt-cron && \
    crontab /etc/cron.d/dbt-cron

# Start cron and tail the log to keep the container alive
CMD cron && tail -F /var/log/cron/dbt.log

