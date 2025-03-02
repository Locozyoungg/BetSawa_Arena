import requests
from flask import current_app
from urllib.parse import quote_plus

class MPesaService:
    """Handle M-Pesa STK Push with retries and Kenyan phone formatting."""
    
    def __init__(self):
        self.consumer_key = current_app.config['MPESA_CONSUMER_KEY']
        self.consumer_secret = current_app.config['MPESA_CONSUMER_SECRET']
        self.callback_url = current_app.config['MPESA_CALLBACK_URL']
    
    def format_phone(self, phone: str) -> str:
        """Convert Kenyan phone to 2547... format."""
        phone = phone.lstrip('0')
        if not phone.startswith('254'):
            phone = f'254{phone}'
        return phone
    
    def stk_push(self, phone: str, amount: float, user_id: int) -> dict:
        """Initiate M-Pesa payment with Safaricom's Daraja API."""
        phone = self.format_phone(phone)
        auth = (self.consumer_key, self.consumer_secret)
        headers = {'Content-Type': 'application/json'}
        payload = {
            'BusinessShortCode': current_app.config['MPESA_SHORTCODE'],
            'Password': quote_plus(current_app.config['MPESA_PASSKEY']),
            'Timestamp': datetime.now().strftime('%Y%m%d%H%M%S'),
            'TransactionType': 'CustomerPayBillOnline',
            'Amount': amount,
            'PartyA': phone,
            'PartyB': current_app.config['MPESA_SHORTCODE'],
            'PhoneNumber': phone,
            'CallBackURL': self.callback_url,
            'AccountReference': f'BETSAWA_{user_id}',
            'TransactionDesc': 'Bet Placement'
        }
        
        # Retry up to 3 times for network issues
        for _ in range(3):
            response = requests.post(
                'https://api.safaricom.co.ke/mpesa/stkpush/v1/processrequest',
                auth=auth,
                json=payload,
                headers=headers
            )
            if response.status_code == 200:
                return response.json()
        raise Exception("M-Pesa API unreachable")
