import React, { useState, useEffect } from 'react';
import { useHistory } from 'react-router-dom';
import { TextField, Button, Select, MenuItem, FormControl, InputLabel } from '@mui/material';
import { createUser, getTiers } from '../services/api';
import { useApiError } from '../hooks/useApiError';

interface Tier {
  id: number;
  name: string;
}

const CreateUserForm: React.FC = () => {
  const [username, setUsername] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [balance, setBalance] = useState('');
  const [referralCode, setReferralCode] = useState('');
  const [tierId, setTierId] = useState('');
  const [tiers, setTiers] = useState<Tier[]>([]);
  const { handleApiError } = useApiError();
  const history = useHistory();

  useEffect(() => {
    const fetchTiers = async () => {
      try {
        const response = await getTiers();
        setTiers(response.data);
      } catch (error) {
        handleApiError(error);
      }
    };

    fetchTiers();
  }, []);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      await createUser({
        username,
        email,
        password,
        balance: balance ? parseFloat(balance) : undefined,
        referral_code: referralCode,
        tier: tierId ? parseInt(tierId) : undefined,
      });
      history.push('/');
    } catch (error) {
      handleApiError(error);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <TextField
        label="Username"
        value={username}
        onChange={(e) => setUsername(e.target.value)}
        required
        fullWidth
        margin="normal"
      />
      <TextField
        label="Email"
        type="email"
        value={email}
        onChange={(e) => setEmail(e.target.value)}
        required
        fullWidth
        margin="normal"
      />
      <TextField
        label="Password"
        type="password"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
        required
        fullWidth
        margin="normal"
      />
      <TextField
        label="Balance"
        type="number"
        value={balance}
        onChange={(e) => setBalance(e.target.value)}
        fullWidth
        margin="normal"
      />
      <TextField
        label="Referral Code"
        value={referralCode}
        onChange={(e) => setReferralCode(e.target.value)}
        fullWidth
        margin="normal"
      />
      <FormControl fullWidth margin="normal">
        <InputLabel>Tier</InputLabel>
        <Select value={tierId} onChange={(e) => setTierId(e.target.value as string)}>
          {tiers.map((tier) => (
            <MenuItem key={tier.id} value={tier.id}>
              {tier.name}
            </MenuItem>
          ))}
        </Select>
      </FormControl>
      <Button type="submit" variant="contained" color="primary">
        Create User
      </Button>
    </form>
  );
};

export default CreateUserForm;

