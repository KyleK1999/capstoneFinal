import React, { useState } from 'react';

function App() {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');

  const register = () => {
    fetch('http://localhost:5555/register', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ username, password }),
    })
    .then(res => res.json())
    .then(data => alert(data.message));
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
    .then(data => alert(data.message));
  };

  return (
    <div>
      <input type="text" placeholder="Username" onChange={e => setUsername(e.target.value)} />
      <input type="password" placeholder="Password" onChange={e => setPassword(e.target.value)} />
      <button onClick={register}>Register</button>
      <button onClick={login}>Login</button>
    </div>
  );
}

export default App;
