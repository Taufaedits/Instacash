import axios from 'axios';

const API_URL = 'http://localhost:8000/api';

const api = axios.create({
  baseURL: API_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

export const getUsers = () => api.get('/users/');
export const createUser = (userData: any) => api.post('/users/create/', userData);
export const getUser = (userId: number) => api.get(`/users/${userId}/`);
export const updateUser = (userId: number, userData: any) => api.put(`/users/${userId}/`, userData);
export const deleteUser = (userId: number) => api.delete(`/users/${userId}/`);

export const getTiers = () => api.get('/tiers/');
export const getTier = (tierId: number) => api.get(`/tiers/${tierId}/`);

export const sendOTP = (email: string) => api.post('/auth/send_otp/', { email });
export const verifyOTP = (email: string, otp: string) => api.post('/auth/verify_otp/', { email, otp });

export default api;

