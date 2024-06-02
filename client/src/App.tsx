import React from 'react';
import { LoginPage } from './pages/LoginPage';
import { SplashPage } from './pages/SplashPage';
import { DashboardPage } from './pages/DashboardPage';
import { Route, Routes } from 'react-router-dom';

function App() {
  return (
    <div>
      <Routes>
        <Route path="/" element={<SplashPage />}></Route>
        <Route path="/login" element={<LoginPage />}></Route>
        <Route path="/dashboard" element={<DashboardPage />}></Route>
      </Routes>
    </div>
  );
}

export default App;
