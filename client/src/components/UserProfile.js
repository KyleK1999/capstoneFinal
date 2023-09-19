import React, { useState, useEffect } from 'react';
import PcHardware from './PcHardware';
import { toast } from 'react-toastify';  // Import the toast functionality

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
      setSavedBuilds(prevBuilds => prevBuilds.filter(build => build.id !== buildId));
      toast.success('Build deleted successfully!');  // Toast for successful deletion
    })
    .catch(error => {
      console.error(`Error occurred: ${error}`);
      toast.error('Failed to delete build.');  // Toast for error case
    });
  };

  return (
    <div className="container mt-5">
      <h2 className="text-center mb-4">Your Saved Builds</h2>
      {savedBuilds.length === 0 && <p className="text-center">No saved builds.</p>}
      {savedBuilds.map((build, index) => {
        const totalPrice = calculateTotalPrice(build.components);
        return (
          <div key={index} className="card mb-3">
            <div className="card-header">
              Build Type: {build.build_type?.type_name || 'N/A'} | Total Price: ${totalPrice || 'N/A'}
            </div>
            <div className="card-body">
              <PcHardware name='CPU' type='cpu' partInfo={build.components.cpu} />
              <PcHardware name='GPU' type='gpu' partInfo={build.components.gpu} />
              <PcHardware name='Memory' type='memory' partInfo={build.components.memory} />
              <PcHardware name='Motherboard' type='motherboard' partInfo={build.components.motherboard} />
              <PcHardware name='Storage' type='storage' partInfo={build.components.storage} />
              <PcHardware name='PSU' type='psu' partInfo={build.components.psu} />
              <PcHardware name='Case' type='case' partInfo={build.components.case} />
              <button className="btn btn-danger mt-2" onClick={() => deleteBuild(build.id)}>Delete</button>
            </div>
          </div>
        );
      })}
    </div>
  );
};

export default UserProfile;
