import React, { useState, useEffect } from 'react';
import PcHardware from './PcHardware'; 
import SaveBuildButton from './SaveBuildButton';

const UserProfile = () => {
  const [savedBuilds, setSavedBuilds] = useState([]);
  const [toggleMoreInfo, setToggleMoreInfo] = useState({});
  const [showMoreInfo, setShowMoreInfo] = useState({});


  useEffect(() => {
    const fetchSavedBuilds = async () => {
      try {
        const response = await fetch('/get_saved_builds');
        if (response.status === 200) {
          const data = await response.json();
          setSavedBuilds(data.savedBuilds);
          //console.log('Current saved builds:', data.savedBuilds); 
        } else {
          console.error('Failed to fetch saved builds');
        }
      } catch (error) {
        console.error('Error fetching saved builds:', error);
      }
    };

    fetchSavedBuilds();
  }, []);

  
  const calculateTotalPrice = (components) => {
    let total = 0;
    for (const key in components) {
      if (components[key] && components[key].price) {
        total += components[key].price;
      }
    }
    return total.toFixed(2);
  };

  const deleteBuild = (buildId) => {
    if (!buildId) {
      console.error('Build ID is undefined.');
      return;
    }
  
    fetch(`/delete_build/${buildId}`, {
      method: 'DELETE',
    })
    .then(response => {
      if (response.ok) {
        return response.json();
      }
      throw new Error('Network response was not ok.');
    })
    .then(data => {
      setSavedBuilds(savedBuilds.filter(build => build.id !== buildId));
    })
    .catch(error => {
      console.error("Failed to delete build:", error);
    });
  };
  
  
  

  return (
    <div>
      <h2>Your Saved Builds</h2>
      <ul>
        {savedBuilds.map((build, index) => {
          console.log("Current build object:", build);
          return (
            <li key={index}>
              <h3>Build Type: {build.build_type?.type_name || 'N/A'}</h3>
              <p>Total Price: ${calculateTotalPrice(build.components) || 'N/A'}</p>
              <div>
                <PcHardware index={index} name='CPU' type='cpu' partInfo={build.components.cpu} toggleMoreInfo={toggleMoreInfo} showMoreInfo={showMoreInfo} />
                <PcHardware index={index} name='GPU' type='gpu' partInfo={build.components.gpu} toggleMoreInfo={toggleMoreInfo} showMoreInfo={showMoreInfo} />  
                <PcHardware index={index} name='Memory' type='memory' partInfo={build.components.memory} toggleMoreInfo={toggleMoreInfo} showMoreInfo={showMoreInfo} />
                <PcHardware index={index} name='Motherboard' type='motherboard' partInfo={build.components.motherboard} toggleMoreInfo={toggleMoreInfo} showMoreInfo={showMoreInfo} />
                <PcHardware index={index} name='Storage' type='storage' partInfo={build.components.storage} toggleMoreInfo={toggleMoreInfo} showMoreInfo={showMoreInfo} />                    
                <PcHardware index={index} name='PSU' type='psu' partInfo={build.components.psu} toggleMoreInfo={toggleMoreInfo} showMoreInfo={showMoreInfo} />       
                <PcHardware index={index} name='Case' type='case' partInfo={build.components.case} toggleMoreInfo={toggleMoreInfo} showMoreInfo={showMoreInfo} />
              </div>
              <button onClick={() => deleteBuild(build.id)}>Delete</button>  
            </li>
          );
        })}
      </ul>
    </div>
  );
  
};

export default UserProfile;
