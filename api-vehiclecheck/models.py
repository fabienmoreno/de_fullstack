from db import db
from datetime import datetime

class Vehicle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    car_registration = db.Column(db.String(20), unique=True, nullable=False)
    date_first_registration = db.Column(db.Date, nullable=False)
    owner_name = db.Column(db.String(100), nullable=False)
    color = db.Column(db.String(50))
    number_of_seats = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def as_dict(self):
        return {
            "id": self.id,
            "car_registration": self.car_registration,
            "date_first_registration": self.date_first_registration.isoformat(),
            "owner_name": self.owner_name,
            "color": self.color,
            "number_of_seats": self.number_of_seats,
            "created_at": self.created_at.isoformat()
        }
