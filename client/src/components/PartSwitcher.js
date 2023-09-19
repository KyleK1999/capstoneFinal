import React, { useState, useEffect } from 'react';
import { Modal, Button } from 'react-bootstrap';
import { formatPart } from './FormatParts';
import PropTypes from 'prop-types';  

const PartSwitcher = ({ buildIndex, partType, switchPart }) => {
  console.log('From PartSwitcher:', typeof switchPart);  
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
      <button 
        className="btn btn-outline-secondary btn-sm rounded-pill"
        onClick={toggleIsOpen}
        style={{ marginRight: '10px' }}
      >
        Want to switch it?
      </button>

      <Modal show={isOpen} onHide={toggleIsOpen}>
        <Modal.Header closeButton>
          <Modal.Title>Switch {partType.toUpperCase()}</Modal.Title>
        </Modal.Header>
        <Modal.Body>
          {parts.map((part, index) => (
            <div key={index}>
              {Object.keys(part).map((key, i) => {
                if (key !== 'id' && key !== 'ProductImage' && key !== 'purchase_link') {
                  return <span key={i} style={{ marginRight: '10px' }}>{key}: {formatPart(key, part[key])}</span>;
                }
                return null;
              })}
              <Button
                variant="outline-primary"
                size="sm"
                className="rounded-pill"
                onClick={() => {
                  switchPart(buildIndex, partType, part);  
                  toggleIsOpen();
                }}
                style={{ marginLeft: '10px' }}
              >
                Switch
              </Button>
            </div>
          ))}
        </Modal.Body>
      </Modal>
    </div>
  );
};

PartSwitcher.propTypes = {
  buildIndex: PropTypes.number.isRequired,
  partType: PropTypes.string.isRequired,
  switchPart: PropTypes.func.isRequired  
};

export default PartSwitcher;
