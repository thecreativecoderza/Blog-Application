from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Initialize the db object
db = SQLAlchemy()

def create_app():
    # Create Flask app instance
    app = Flask(__name__)

    # Set configuration
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize the db with the app
    db.init_app(app)

    # Register blueprints or routes (if any)
    from app.routes import routes
    app.register_blueprint(routes)

    return app
