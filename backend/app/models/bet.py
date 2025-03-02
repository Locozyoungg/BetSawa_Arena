# Database model for bet transactions
from backend.app.extensions import db

class Bet(db.Model):
    """Stores all betting transactions with blockchain verification"""
    __tablename__ = 'bets'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    prediction = db.Column(db.String(200),  # Sanitized input
    tx_hash = db.Column(db.String(66),  # Blockchain transaction hash
    created_at = db.Column(db.DateTime, default=db.func.now())
    status = db.Column(db.String(20), default='pending')  # won/lost/pending

    # Index for faster querying
    __table_args__ = (
        db.Index('idx_user_status', 'user_id', 'status'),
    )
