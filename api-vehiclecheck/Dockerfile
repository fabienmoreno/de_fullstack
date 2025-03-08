# Use a slim Python base image
FROM python:3.10-slim

# Create a working directory
WORKDIR /app

# Install system dependencies (for psycopg2)
RUN apt-get update && apt-get install -y \
    libpq-dev gcc && rm -rf /var/lib/apt/lists/*

# Copy requirements file into container
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . /app

# Expose port 5000 (Flask default)
EXPOSE 5000

# By default, get DB env variables from docker-compose
CMD ["python3", "app.py"]
