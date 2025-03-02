# Flask application factory
from flask import Flask
from .extensions import db, jwt, limiter
from .config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize extensions
    db.init_app(app)
    jwt.init_app(app)
    limiter.init_app(app)

    # Register blueprints
    from .routes.auth import auth_bp
    from .routes.bets import bets_bp
    app.register_blueprint(auth_bp)
    app.register_blueprint(bets_bp)

    # Create tables
    with app.app_context():
        db.create_all()

    return app
