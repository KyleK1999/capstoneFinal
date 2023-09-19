import React, { useState } from 'react';
import { formatPart } from './FormatParts';
import { toast } from 'react-toastify';
import PartSwitcher from './PartSwitcher';
import { Modal } from 'react-bootstrap';  

  const PcHardware = ({ buildIndex, index, name, type, partInfo, toggleMoreInfo, showMoreInfo, switchPart, showSwitch }) => {
  const [moreInfoModalOpen, setMoreInfoModalOpen] = useState(false);  
  const key = `${index}_${type}`;

  const productImage = partInfo?.ProductImage ?? '';
  const productName = partInfo?.name ?? 'N/A';
  const purchaseLink = partInfo?.purchase_link ?? '#';

  const handleMoreInfo = () => {
    if (!partInfo) {
      toast.error("No part info available");
    } else {
      setMoreInfoModalOpen(true);  
    }
  };

  return (
    <div className="mb-3 d-flex align-items-center">
      <img src={productImage} alt={productName} width="100" height="100" style={{ marginRight: '20px' }}/>
      <span style={{ marginRight: '20px' }}>{name}: {productName}</span>
      <button className="btn btn-outline-primary btn-sm rounded-pill" onClick={handleMoreInfo} style={{ marginRight: '10px' }}>More Info</button>
      {showSwitch && <PartSwitcher buildIndex={buildIndex} partType={type} switchPart={switchPart} style={{ marginRight: '40px' }} />}
      <a className="btn btn-outline-success btn-sm rounded-pill" href={purchaseLink} target="_blank" rel="noopener noreferrer">Purchase</a>
      {showMoreInfo && showMoreInfo[key] ? (
        <div className="mt-2">
          {Object.keys(partInfo ?? {}).map((infoKey, i) => (
            infoKey !== 'ProductImage' && infoKey !== 'purchase_link' && infoKey !== 'name' && infoKey !== 'id' ?
              <span key={i} className="d-block mb-1">
                {infoKey}: {formatPart(infoKey, partInfo[infoKey])}
              </span>
              : null
          ))}
        </div>
      ) : null}
      
      {/* More Info Modal */}
      <Modal show={moreInfoModalOpen} onHide={() => setMoreInfoModalOpen(false)}>
        <Modal.Header closeButton>
          <Modal.Title>{productName} Info</Modal.Title>
        </Modal.Header>
        <Modal.Body>
          {Object.keys(partInfo ?? {}).map((infoKey, i) => (
            infoKey !== 'ProductImage' && infoKey !== 'purchase_link' && infoKey !== 'name' && infoKey !== 'id' ?
              <span key={i} className="d-block mb-1">
                {infoKey}: {formatPart(infoKey, partInfo[infoKey])}
              </span>
              : null
          ))}
        </Modal.Body>
      </Modal>
    </div>
  );
};

export default PcHardware;
