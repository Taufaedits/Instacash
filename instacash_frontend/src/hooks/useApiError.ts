import { useState } from 'react';
import { useSnackbar } from 'notistack';

export const useApiError = () => {
  const [error, setError] = useState<string | null>(null);
  const { enqueueSnackbar } = useSnackbar();

  const handleApiError = (error: any) => {
    const errorMessage = error.response?.data?.message || 'An error occurred';
    setError(errorMessage);
    enqueueSnackbar(errorMessage, { variant: 'error' });
  };

  return { error, setError, handleApiError };
};

