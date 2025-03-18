from flask import Flask
from config import Config
from db import db
from routes import bp
from flask_migrate import Migrate

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize extensions
    db.init_app(app)
    Migrate(app, db)

    # Register Blueprints
    app.register_blueprint(bp, url_prefix="/api")

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=5000)
