FROM ghcr.io/dbt-labs/dbt-postgres:1.6.0

WORKDIR /usr/app

# --- Diagnostic Commands (Add these) ---
RUN echo "Current directory contents:"
RUN ls -la .
RUN echo "dbt_project.yml content:"
RUN cat dbt_project.yml
# --- End Diagnostic Commands ---

COPY . .