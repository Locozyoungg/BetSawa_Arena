# Environment configuration
import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # PostgreSQL configuration
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    
    # JWT settings
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
    JWT_ACCESS_TOKEN_EXPIRES = 3600  # 1 hour
    
    # M-Pesa credentials
    MPESA_CONSUMER_KEY = os.getenv('MPESA_CONSUMER_KEY')
    MPESA_CONSUMER_SECRET = os.getenv('MPESA_CONSUMER_SECRET')
    
    # Rate limiting
    RATELIMIT_STORAGE_URI = 'redis://redis:6379/0'
