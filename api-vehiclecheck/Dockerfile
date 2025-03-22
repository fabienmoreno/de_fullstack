FROM python:3.11-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy your app code into container
COPY . /app

EXPOSE 5000

# This will handle migration generation automatically
CMD ["sh", "-c", "\
    flask db init 2>/dev/null || true && \
    flask db migrate -m 'Docker Auto Migration' && \
    flask db upgrade && \
    python app.py \
"]
