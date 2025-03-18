from flask import Blueprint, request, jsonify
from db import db
from models import Vehicle
from datetime import datetime

bp = Blueprint('api', __name__)

@bp.route('/health', methods=['GET'])
def health_check():
    return jsonify({"message": "API is running"}), 200

@bp.route('/vehicles', methods=['POST'])
def add_vehicle():
    data = request.get_json()
    
    # Validate required fields
    for field in ['car_registration', 'date_first_registration', 'owner_name']:
        if field not in data:
            return jsonify({"error": f"Missing field: {field}"}), 400

    try:
        date_first_registration = datetime.strptime(data['date_first_registration'], "%Y-%m-%d").date()
    except ValueError:
        return jsonify({"error": "Invalid date format. Use YYYY-MM-DD."}), 400

    number_of_seats = data.get('number_of_seats')
    if number_of_seats:
        try:
            number_of_seats = int(number_of_seats)
            if number_of_seats <= 0:
                raise ValueError
        except ValueError:
            return jsonify({"error": "number_of_seats must be a positive integer"}), 400

    vehicle = Vehicle(
        car_registration=data['car_registration'],
        date_first_registration=date_first_registration,
        owner_name=data['owner_name'],
        color=data.get('color'),
        number_of_seats=number_of_seats
    )

    try:
        db.session.add(vehicle)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Vehicle could not be added", "details": str(e)}), 500

    return jsonify(vehicle.as_dict()), 201

@bp.route('/vehicles/<int:vehicle_id>', methods=['GET'])
def get_vehicle_by_id(vehicle_id):
    vehicle = Vehicle.query.get(vehicle_id)
    if not vehicle:
        return jsonify({"error": "Vehicle not found"}), 404
    return jsonify(vehicle.as_dict()), 200

@bp.route('/vehicles/registration/<car_reg>', methods=['GET'])
def get_vehicle_by_registration(car_reg):
    vehicle = Vehicle.query.filter_by(car_registration=car_reg).first()
    if not vehicle:
        return jsonify({"error": "Vehicle not found"}), 404
    return jsonify(vehicle.as_dict()), 200
