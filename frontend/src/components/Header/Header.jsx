// Header.js
import React from 'react';
import { Link } from 'react-router-dom';
import './Header.css'; // Import the CSS file

const Header = () => {
  return (
    <div className="header-container">
      <div className="logo-container">
        <span className="logo">BIZ-HUB</span>
        <div children className='nav-links'>
          <ul>
            <li><Link to ='/' >Home</Link></li>
            <li><Link to ='Login'>Login</Link></li>
          </ul>
        </div>
      </div>
      <div className="login-text">
        <Link to="/Register">Register as a BIZ Owner</Link>
      </div>
    </div>
  );
};

export default Header;
