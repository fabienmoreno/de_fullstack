FROM ghcr.io/dbt-labs/dbt-postgres:1.6.0

WORKDIR /usr/app

# --- EXTREME Diagnostic Commands ---
RUN echo "Initial working directory: $(pwd)"
RUN echo "Files in root (/):"
RUN ls -la /
RUN echo "Files in /usr:"
RUN ls -la /usr
RUN echo "Files in /usr/app (before COPY):"
RUN ls -la .
RUN echo "Attempting to cat dbt_project.yml:"
RUN cat dbt_project.yml
# --- End Diagnostic Commands ---

COPY . .

# --- More Diagnostics AFTER COPY ---
RUN echo "Files in /usr/app (after COPY):"
RUN ls -la .