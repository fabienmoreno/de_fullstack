FROM ghcr.io/dbt-labs/dbt-postgres:1.6.0

WORKDIR /usr/app

# Copy all dbt files to working directory
COPY . /usr/app/

# Explicitly create directory and copy profiles.yml
RUN mkdir -p /root/.dbt
COPY profiles.yml /root/.dbt/profiles.yml

# Install dependencies
RUN dbt deps

ENTRYPOINT ["dbt"]
CMD ["run"]
