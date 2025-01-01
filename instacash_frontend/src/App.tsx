import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import { ThemeProvider, createTheme } from '@mui/material/styles';
import CssBaseline from '@mui/material/CssBaseline';
import { SnackbarProvider } from 'notistack';
import { AuthProvider } from './context/AuthContext';
import UserList from './components/UserList';
import CreateUserForm from './components/CreateUserForm';
import OTPRequestForm from './components/OTPRequestForm';
import OTPVerificationForm from './components/OTPVerificationForm';

const theme = createTheme();

function App() {
  return (
    <ThemeProvider theme={theme}>
      <CssBaseline />
      <SnackbarProvider maxSnack={3}>
        <AuthProvider>
          <Router>
            <Switch>
              <Route exact path="/" component={UserList} />
              <Route path="/create-user" component={CreateUserForm} />
              <Route path="/request-otp" component={OTPRequestForm} />
              <Route path="/verify-otp" component={OTPVerificationForm} />
            </Switch>
          </Router>
        </AuthProvider>
      </SnackbarProvider>
    </ThemeProvider>
  );
}

export default App;

