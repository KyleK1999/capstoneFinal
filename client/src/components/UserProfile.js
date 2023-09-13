import React, { useState, useEffect } from 'react';

const UserProfile = () => {
  const [savedBuilds, setSavedBuilds] = useState([]);

  useEffect(() => {
    const fetchSavedBuilds = async () => {
      try {
        const response = await fetch('/get_saved_builds'); 
        if (response.status === 200) {
          const data = await response.json();
          setSavedBuilds(data.savedBuilds);
        } else {
          console.error('Failed to fetch saved builds');
        }
      } catch (error) {
        console.error('Error fetching saved builds:', error);
      }
    };

    fetchSavedBuilds();
  }, []);

  return (
    <div>
      <h2>Your Saved Builds</h2>
      <ul>
        {savedBuilds.map((build, index) => (
          <li key={index}>
            <p>Build Type: {build.build_type || 'N/A'}</p>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default UserProfile;
