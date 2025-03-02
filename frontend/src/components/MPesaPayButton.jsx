// Reusable M-Pesa payment component
import React from 'react';
import { useTranslation } from 'react-i18next';
import { useEncryptedMPesa } from '../hooks/useEncryptedMPesa';

const MPesaPayButton = ({ amount, onSuccess }) => {
  const { t } = useTranslation();
  const [encryptedData, encrypt] = useEncryptedMPesa();

  const handlePayment = async () => {
    try {
      // Encrypt M-Pesa details
      encrypt(amount);
      await axios.post('/api/payments/mpesa', { data: encryptedData });
      onSuccess();
    } catch (error) {
      alert(t('payment_error'));
    }
  };

  return (
    <button 
      className="mpesa-button"
      onClick={handlePayment}
    >
      {t('pay_with_mpesa')}
    </button>
  );
};
