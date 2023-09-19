import React, { useEffect, useState } from 'react';
import PcHardware from './PcHardware';
// import PartSwitcher from './PartSwitcher'; 
import SaveBuildButton from './SaveBuildButton';
import { toast } from 'react-toastify';

function DisplayBuilds(props) {
  const [builds, setBuilds] = useState([]);
  const [error, setError] = useState(null);
  const [showMoreInfo, setShowMoreInfo] = useState({});
  

  useEffect(() => {
    const fetchData = async () => {
      const urlParams = new URLSearchParams(window.location.search);
      const minPrice = urlParams.get('minPrice');
      const maxPrice = urlParams.get('maxPrice');

      try {
        const response = await fetch(`http://localhost:5555/get_builds?minPrice=${minPrice}&maxPrice=${maxPrice}`);
        
        if (response.ok) {
          const data = await response.json();
          console.log("Data from API:", data);
          console.log("Data from API:", data);
          setBuilds(data.builds);
          setError(null);
        } else {
          throw new Error('Server response not OK');
        }
      } catch (err) {
        console.error('Error:', err);
        toast.error("Could not fetch builds."); 
        setError('Could not fetch builds.');
      }
    };

    fetchData();
  }, []);

  const switchPart = (buildIndex, partType, selectedPart) => {
    console.log('From DisplayBuilds:', typeof switchPart);
    const updatedBuilds = [...builds];
    const buildToUpdate = updatedBuilds[buildIndex];
    if (buildToUpdate && buildToUpdate.components) {
      if (partType in buildToUpdate.components) {
        buildToUpdate.components[partType] = selectedPart;
        buildToUpdate.totalPrice = calculateTotalPrice(buildToUpdate.components);
        updatedBuilds[buildIndex] = buildToUpdate;
        setBuilds(updatedBuilds);
      } else {
        console.error(`Part type not found: ${partType}`);
      }
    }
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

  const toggleMoreInfo = (index, part) => {
    const key = `${index}_${part}`;
    setShowMoreInfo(prevState => ({
      ...prevState,
      [key]: !prevState[key]
    }));
  };

  console.log('From DisplayBuilds:', typeof switchPart); 

  return (
    <div className="container mt-5">
      <h2 className="text-center mb-4">Builds</h2>
      {error && (
        <div className="alert alert-danger" role="alert">
          Error: {error}
        </div>
      )}
      {Array.isArray(builds) && builds.length > 0 ? (
        builds.map((build, index) => {
          const totalPrice = calculateTotalPrice(build.components);
          
          return (
            <div key={index} className="card mb-3">
              <div className="card-header">
                Build Type: {build.build_type || 'N/A'} | Total Price: ${totalPrice}
              </div>
              <div className="card-body">
                <PcHardware index={index} buildIndex={index} name='CPU' type='cpu' partInfo={build.components.cpu} switchPart={switchPart} toggleMoreInfo={toggleMoreInfo} showMoreInfo={showMoreInfo} showSwitch={true} />
                <PcHardware index={index} buildIndex={index} name='GPU' type='gpu' partInfo={build.components.gpu} switchPart={switchPart} toggleMoreInfo={toggleMoreInfo} showMoreInfo={showMoreInfo} showSwitch={true} />
                <PcHardware index={index} buildIndex={index} name='Memory' type='memory' partInfo={build.components.memory} switchPart={switchPart} toggleMoreInfo={toggleMoreInfo} showMoreInfo={showMoreInfo} showSwitch={true} />
                <PcHardware index={index} buildIndex={index} name='Motherboard' type='motherboard' partInfo={build.components.motherboard} switchPart={switchPart} toggleMoreInfo={toggleMoreInfo} showMoreInfo={showMoreInfo} showSwitch={true} />
                <PcHardware index={index} buildIndex={index} name='Storage' type='storage' partInfo={build.components.storage} switchPart={switchPart} toggleMoreInfo={toggleMoreInfo} showMoreInfo={showMoreInfo} showSwitch={true} />
                <PcHardware index={index} buildIndex={index} name='PSU' type='psu' partInfo={build.components.psu} switchPart={switchPart} toggleMoreInfo={toggleMoreInfo} showMoreInfo={showMoreInfo} showSwitch={true} />
                <PcHardware index={index} buildIndex={index} name='Case' type='case' partInfo={build.components.case} switchPart={switchPart} toggleMoreInfo={toggleMoreInfo} showMoreInfo={showMoreInfo} showSwitch={true} />
                
                <SaveBuildButton buildDetails={build} />
              </div>
            </div>
          );
        })
      ) : (
        <div className="text-center">
          Loading...
        </div>
      )}
    </div>
  );
}

export default DisplayBuilds;
