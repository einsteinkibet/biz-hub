import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Header from './components/Header/Header';
import Sidebar from './components/Sidebar/Sidebar';
import Home from './components/Home/Home';
import Login from './components/Login/Login';
import Register from './components/Register/Register';
import Userpage from './components/Userpage/Userpage';
import './App.css';

const App = () => {
  return (
    <Router>
      <div>
        <Header />
        <div style={{ display: 'flex' }}>
          <Sidebar />
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/login" element={<Login />} />
            <Route path="/register" element={<Register />} />
            <Route path="/user" element={<Userpage />} />
          </Routes>
        </div>
      </div>
    </Router>
  );
};

export default App;
