import React, { useState, useEffect } from 'react';
import { formatPart } from './FormatParts';

const PartSwitcher = ({ buildIndex, partType, switchPart }) => {
  const [isOpen, setIsOpen] = useState(false);
  const [parts, setParts] = useState([]);

  useEffect(() => {
    const fetchParts = async () => {
      const response = await fetch(`http://localhost:5555/get_parts?type=${partType}`);
      const data = await response.json();
      setParts(data ?? []);
    };

    fetchParts();
  }, [partType]);

  const toggleIsOpen = () => {
    setIsOpen(!isOpen);
  };

  return (
    <div>
      <button onClick={toggleIsOpen}>Want to switch it?</button>
      {isOpen && (
        <div className="popup">
          {parts.map((part, index) => (
            <div key={index}>
              {Object.keys(part).map((key, i) => {
                if (key !== 'id' && key !== 'ProductImage' && key !== 'purchase_link') {
                  return <span key={i} style={{ marginRight: '10px' }}>{key}: {formatPart(key, part[key])}</span>; 
                }
                return null;
              })}
              <button onClick={() => {
                switchPart(buildIndex, partType, part);
                setIsOpen(false);
              }} style={{ marginLeft: '10px' }}>Switch</button>  
            </div>
          ))}
        </div>
      )}
    </div>
  );
};

export default PartSwitcher;
