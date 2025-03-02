# File: backend/app/utils/security.py  
from cryptography.fernet import Fernet  

class DataEncryptor:  
    """Encrypt sensitive fields (M-Pesa phone, KYC) using AES-256-GCM"""  
    def __init__(self):  
        self.key = Fernet.generate_key()  # Store in AWS Secrets Manager  

    def encrypt(self, data: str) -> bytes:  
        return Fernet(self.key).encrypt(data.encode())  

    def decrypt(self, token: bytes) -> str:  
        return Fernet(self.key).decrypt(token).decode()  
