from datetime import datetime
from backend.app.extensions import db

class User(db.Model):
    """User model with KYC and M-Pesa details (encrypted)."""
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    # Encrypted using AES-256-GCM
    _mpesa_phone = db.Column(db.String(200), nullable=False)
    _id_number = db.Column(db.String(200))  # KYC field
    xp_points = db.Column(db.Integer, default=0)
    daily_limit = db.Column(db.Float, default=50000)  # BCLB compliance
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Relationships
    bets = db.relationship('Bet', backref='user', lazy=True)
    casino_sessions = db.relationship('CasinoSession', backref='user', lazy=True)
