import React from 'react';
import { LoginPage } from './pages/LoginPage';
import { SplashPage } from './pages/SplashPage';
import { DashboardPage } from './pages/DashboardPage';
import  { ProfilePage } from './pages/ProfilePage';
import { Route, Routes } from 'react-router-dom';

function App() {
  return (
    <div>
      <Routes>
        {/* <Route path="/" element={<SplashPage />}></Route> */}
        <Route path="/login" element={<LoginPage />}></Route>
        <Route path="/dashboard" element={<DashboardPage />}></Route>
        <Route path="/profile" element={<ProfilePage />}></Route>
      </Routes>
    </div>
  );
}

export default App;
