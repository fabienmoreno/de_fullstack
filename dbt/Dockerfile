FROM ghcr.io/dbt-labs/dbt-postgres:1.6.0

# Set working directory
WORKDIR /usr/app

# Copy dbt_project.yml and all dbt files to the container
COPY . /usr/app/

# Verify the file is copied correctly (optional debug)
RUN ls -la /usr/app
RUN cat /usr/app/dbt_project.yml

# Install dependencies if you have any (optional)
RUN dbt deps

# Final command to run dbt
CMD ["dbt", "run"]
