import os
from flask import Flask, request, jsonify
import psycopg2
from psycopg2 import sql

app = Flask(__name__)

# Read DB connection details from environment variables
DB_HOST = os.environ.get('DB_HOST', 'postgres')
DB_PORT = os.environ.get('DB_PORT', '5432')
DB_USER = os.environ.get('DB_USER', 'postgres')
DB_PASSWORD = os.environ.get('DB_PASSWORD', 'password')
DB_NAME = os.environ.get('DB_NAME', 'main_db')

# Create a connection function
def get_connection():
    return psycopg2.connect(
        host=DB_HOST,
        port=DB_PORT,
        user=DB_USER,
        password=DB_PASSWORD,
        dbname=DB_NAME
    )

# OPTIONAL: Initialize table on startup (quick & dirty approach)
# In production, you'd typically use migrations or a dedicated init script.
def init_table():
    conn = get_connection()
    cur = conn.cursor()
    create_table_query = """
    CREATE TABLE IF NOT EXISTS vehicles (
        id SERIAL PRIMARY KEY,
        date_of_check DATE,
        color VARCHAR(50) NOT NULL,
        brand VARCHAR(100) NULL
    )
    """
    cur.execute(create_table_query)
    conn.commit()
    cur.close()
    conn.close()

@app.route('/vehicle', methods=['POST'])
def create_vehicle():
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Invalid JSON'}), 400

    date_of_check = data.get('date_of_check')  # can be None
    color = data.get('color')
    brand = data.get('brand')  # optional

    if not color:
        return jsonify({'error': 'Vehicle color is mandatory'}), 400

    try:
        conn = get_connection()
        cur = conn.cursor()
        insert_query = """
            INSERT INTO vehicles (date_of_check, color, brand)
            VALUES (%s, %s, %s)
            RETURNING id;
        """
        cur.execute(insert_query, (date_of_check, color, brand))
        new_id = cur.fetchone()[0]
        conn.commit()
        cur.close()
        conn.close()
    except Exception as e:
        return jsonify({'error': str(e)}), 500

    return jsonify({'message': 'Vehicle created', 'id': new_id}), 201

@app.route('/vehicle/<int:vehicle_id>', methods=['GET'])
def get_vehicle(vehicle_id):
    try:
        conn = get_connection()
        cur = conn.cursor()
        select_query = """
            SELECT id, date_of_check, color, brand
            FROM vehicles
            WHERE id = %s
        """
        cur.execute(select_query, (vehicle_id,))
        row = cur.fetchone()
        cur.close()
        conn.close()

        if row is None:
            return jsonify({'error': 'Vehicle not found'}), 404

        # row -> (id, date_of_check, color, brand)
        vehicle_data = {
            'id': row[0],
            'date_of_check': str(row[1]) if row[1] else None,
            'color': row[2],
            'brand': row[3]
        }
        return jsonify(vehicle_data), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Initialize table for quick demo. In real usage, handle migrations properly.
    init_table()

    # Start Flask app on port 5000
    app.run(host='0.0.0.0', port=5000, debug=False)
