import React, { useState, useEffect } from 'react';

const SaveBuildButton = ({ buildDetails }) => {
  const [username, setUsername] = useState('');

  useEffect(() => {
    const usernameCookie = document.cookie.split('; ').find(row => row.startsWith('username='));
    const extractedUsername = usernameCookie ? usernameCookie.split('=')[1] : null;
    setUsername(extractedUsername);
  }, []);

  const saveBuild = async () => {
    if (!username) {
      alert("You need to login first!");
      return;
    }

    try {
      const response = await fetch('/save_build', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          username,
          build: buildDetails,
        }),
      });

      const data = await response.json();
      if (response.status === 200) {
        alert(data.message);
      } else {
        alert(data.message); 
      }
    } catch (error) {
      console.error("There was a problem with the fetch operation:", error);
    }
  };

  return (
    <button onClick={saveBuild}>Save Build</button>
  );
};

export default SaveBuildButton;
