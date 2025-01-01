import React, { useState } from 'react';
import { useHistory } from 'react-router-dom';
import { TextField, Button } from '@mui/material';
import { sendOTP } from '../services/api';
import { useApiError } from '../hooks/useApiError';

const OTPRequestForm: React.FC = () => {
  const [email, setEmail] = useState('');
  const { handleApiError } = useApiError();
  const history = useHistory();

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      await sendOTP(email);
      history.push('/verify-otp', { email });
    } catch (error) {
      handleApiError(error);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <TextField
        label="Email"
        type="email"
        value={email}
        onChange={(e) => setEmail(e.target.value)}
        required
        fullWidth
        margin="normal"
      />
      <Button type="submit" variant="contained" color="primary">
        Request OTP
      </Button>
    </form>
  );
};

export default OTPRequestForm;

