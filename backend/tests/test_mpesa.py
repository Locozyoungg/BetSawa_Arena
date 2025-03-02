# Test M-Pesa integration
import pytest
from unittest.mock import patch
from app.services.mpesa import MPesaService

@patch('requests.post')
def test_mpesa_stk_push(mock_post):
    mock_post.return_value.status_code = 200
    mock_post.return_value.json.return_value = {'CheckoutRequestID': 'test123'}
    
    mpesa = MPesaService()
    response = mpesa.stk_push('0712345678', 100, 1)
    
    assert 'test123' in response['CheckoutRequestID']
    assert mock_post.call_count == 1
