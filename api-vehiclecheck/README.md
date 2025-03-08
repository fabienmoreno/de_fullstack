# Vehicle Check API

This is a simple Flask API service to track vehicles checked on the street.

## Endpoints

- **POST /vehicle**
  - Request body (JSON):
    ```json
    {
      "date_of_check": "YYYY-MM-DD",
      "color": "red",
      "brand": "Toyota"
    }
    ```
  - Response:
    ```json
    {
      "message": "Vehicle created",
      "id": <new_record_id>
    }
    ```

- **GET /vehicle/<id>**
  - Response (JSON):
    ```json
    {
      "id": 123,
      "date_of_check": "2025-03-08",
      "color": "red",
      "brand": "Toyota"
    }
    ```
    or a 404 if not found.

## Environment Variables

- `DB_HOST` (default: `postgres`)
- `DB_PORT` (default: `5432`)
- `DB_USER` (default: `postgres`)
- `DB_PASSWORD` (default: `password`)
- `DB_NAME` (default: `main_db`)

## How to Run Locally

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
