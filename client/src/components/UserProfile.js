import React, { useState, useEffect } from 'react';
import PcHardware from './PcHardware';

const UserProfile = () => {
  const [savedBuilds, setSavedBuilds] = useState([]);
  const [toggleMoreInfo, setToggleMoreInfo] = useState({});

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

  const toggleMoreInfoFunc = (index, type) => {
    setToggleMoreInfo(prevState => ({
      ...prevState,
      [`${index}_${type}`]: !prevState[`${index}_${type}`],
    }));
  };

  const calculateTotalPrice = (components) => {
    let total = 0;
    for (const key in components) {
      if (components[key] && components[key].Price) {
        total += components[key].Price;
      }
    }
    return total.toFixed(2);
  };

  const deleteBuild = (buildId) => {
    if (!buildId) {
      console.error('Build ID is undefined');
      return;
    }

    fetch(`/delete_build/${buildId}`, {
      method: 'DELETE',
    })
    .then(res => res.json())
    .then(data => {
      // Remove the deleted build from state
      setSavedBuilds(prevBuilds => prevBuilds.filter(build => build.id !== buildId));
    })
    .catch(error => {
      console.error(`Error occurred: ${error}`);
    });
  };

  return (
    <div>
      <h2>Your Saved Builds</h2>
      <ul>
        {savedBuilds.map((build, index) => {
          return (
            <li key={index}>
              <h3>Build Type: {build.build_type?.type_name || 'N/A'}</h3>
              <p>Total Price: ${calculateTotalPrice(build.components) || 'N/A'}</p>
              <div>
                <PcHardware index={index} name='CPU' type='cpu' partInfo={build.components.cpu} toggleMoreInfo={toggleMoreInfoFunc} showMoreInfo={toggleMoreInfo} />
                <PcHardware index={index} name='GPU' type='gpu' partInfo={build.components.gpu} toggleMoreInfo={toggleMoreInfoFunc} showMoreInfo={toggleMoreInfo} />  
                <PcHardware index={index} name='Memory' type='memory' partInfo={build.components.memory} toggleMoreInfo={toggleMoreInfoFunc} showMoreInfo={toggleMoreInfo} />
                <PcHardware index={index} name='Motherboard' type='motherboard' partInfo={build.components.motherboard} toggleMoreInfo={toggleMoreInfoFunc} showMoreInfo={toggleMoreInfo} />
                <PcHardware index={index} name='Storage' type='storage' partInfo={build.components.storage} toggleMoreInfo={toggleMoreInfoFunc} showMoreInfo={toggleMoreInfo} />                    
                <PcHardware index={index} name='PSU' type='psu' partInfo={build.components.psu} toggleMoreInfo={toggleMoreInfoFunc} showMoreInfo={toggleMoreInfo} />       
                <PcHardware index={index} name='Case' type='case' partInfo={build.components.case} toggleMoreInfo={toggleMoreInfoFunc} showMoreInfo={toggleMoreInfo} />
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
