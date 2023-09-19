import React, { useState } from 'react';
import { useHistory } from 'react-router-dom';
import { toast } from 'react-toastify';

function Login() {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const history = useHistory();

  const showToast = (message, type = "info") => {
    toast(message, {
      type,
      position: "top-right",
      autoClose: 5000,
      hideProgressBar: false,
      closeOnClick: true,
      pauseOnHover: true,
      draggable: true,
    });
  };

  const login = () => {
    fetch('http://localhost:5555/login', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ username, password }),
      credentials: 'include',
    })
    .then(res => res.json())
    .then(data => {
      showToast(data.message, data.message === 'Logged in successfully!' ? 'success' : 'error');
      if (data.message === 'Logged in successfully!') {
        history.push('/select_price_range');
      }
    });
  };

  const register = () => {
    fetch('http://localhost:5555/register', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ username, password }),
    })
    .then(res => res.json())
    .then(data => showToast(data.message));
  };

  return (
    <div className="container mt-5">
      <div className="row justify-content-center">
        <div className="col-md-4">
          <h2 className="text-center">Login</h2>
          <div className="form-group mt-3">
            <input 
              type="text" 
              className="form-control mb-4" 
              placeholder="Username" 
              onChange={e => setUsername(e.target.value)}
            />
          </div>
          <div className="form-group">
            <input 
              type="password" 
              className="form-control mb-4" 
              placeholder="Password" 
              onChange={e => setPassword(e.target.value)} 
            />
          </div>
          <div className="d-flex justify-content-center">
            <button className="btn btn-primary" style={{marginRight: '15px'}} onClick={register}>Register</button>
            <button className="btn btn-success" style={{marginLeft: '15px'}} onClick={login}>Login</button>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Login;
