import React, { useEffect, useState } from 'react';
import PcHardware from './PcHardware';
import PartSwitcher from './PartSwitcher'; 
import SaveBuildButton from './SaveBuildButton';

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
        setError('Could not fetch builds.');
      }
    };

    fetchData();
  }, []);

  const switchPart = (buildIndex, partType, selectedPart) => {
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

  return (
    <div>
      <h2>Builds</h2>
      {error && <p>Error: {error}</p>}
      {Array.isArray(builds) && builds.length > 0 ? (
        builds.map((build, index) => {
          if (!build || !build.components) {
            return <div key={index}>This build or its components are undefined or null.</div>;
          }
          
          const { cpu, gpu, memory, motherboard, storage, psu, case: caseItem } = build.components;
          const totalPrice = calculateTotalPrice(build.components);

          return (
            <div key={index}>
              <h3>Build Type: {build.build_type || 'N/A'} | Total Price: ${totalPrice}</h3>
              <div>
                <PcHardware index={index} name='CPU' type='cpu' partInfo={cpu} toggleMoreInfo={toggleMoreInfo} showMoreInfo={showMoreInfo} />
                <PartSwitcher buildIndex={index} partType='cpu' switchPart={switchPart} />
                
                <PcHardware index={index} name='GPU' type='gpu' partInfo={gpu} toggleMoreInfo={toggleMoreInfo} showMoreInfo={showMoreInfo} />
                <PartSwitcher buildIndex={index} partType='gpu' switchPart={switchPart} />

                <PcHardware index={index} name='Memory' type='memory' partInfo={memory} toggleMoreInfo={toggleMoreInfo} showMoreInfo={showMoreInfo} />
                <PartSwitcher buildIndex={index} partType='memory' switchPart={switchPart} />

                <PcHardware index={index} name='Motherboard' type='motherboard' partInfo={motherboard} toggleMoreInfo={toggleMoreInfo} showMoreInfo={showMoreInfo} />
                <PartSwitcher buildIndex={index} partType='motherboard' switchPart={switchPart} />

                <PcHardware index={index} name='Storage' type='storage' partInfo={storage} toggleMoreInfo={toggleMoreInfo} showMoreInfo={showMoreInfo} />
                <PartSwitcher buildIndex={index} partType='storage' switchPart={switchPart} />

                <PcHardware index={index} name='PSU' type='psu' partInfo={psu} toggleMoreInfo={toggleMoreInfo} showMoreInfo={showMoreInfo} />
                <PartSwitcher buildIndex={index} partType='psu' switchPart={switchPart} />

                <PcHardware index={index} name='Case' type='case' partInfo={caseItem} toggleMoreInfo={toggleMoreInfo} showMoreInfo={showMoreInfo} />
                <PartSwitcher buildIndex={index} partType='case' switchPart={switchPart} />
                <SaveBuildButton buildDetails={build} />
              </div>
            </div>
          );
        })
      ) : (
        'Loading...'
      )}
    </div>
  );
}

export default DisplayBuilds;
