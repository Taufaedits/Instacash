import React, { useState } from 'react';
import { useHistory, useLocation } from 'react-router-dom';
import { TextField, Button } from '@mui/material';
import { verifyOTP } from '../services/api';
import { useApiError } from '../hooks/useApiError';
import { useAuth } from '../context/AuthContext';

const OTPVerificationForm: React.FC = () => {
  const [otp, setOtp] = useState('');
  const { handleApiError } = useApiError();
  const history = useHistory();
  const location = useLocation<{ email: string }>();
  const { setIsAuthenticated } = useAuth();

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      await verifyOTP(location.state.email, otp);
      setIsAuthenticated(true);
      history.push('/');
    } catch (error) {
      handleApiError(error);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <TextField
        label="OTP"
        value={otp}
        onChange={(e) => setOtp(e.target.value)}
        required
        fullWidth
        margin="normal"
      />
      <Button type="submit" variant="contained" color="primary">
        Verify OTP
      </Button>
    </form>
  );
};

export default OTPVerificationForm;

