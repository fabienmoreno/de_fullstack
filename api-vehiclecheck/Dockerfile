FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# explicitly copy migrations
COPY migrations ./migrations

# copy rest of your app code
COPY . /app

EXPOSE 5000

CMD ["sh", "-c", "flask db upgrade && python app.py"]
