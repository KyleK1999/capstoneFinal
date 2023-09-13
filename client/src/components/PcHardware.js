import React from 'react';
import { formatPart } from './FormatParts'; 

const PcHardware = ({ index, name, type, partInfo, toggleMoreInfo, showMoreInfo }) => {
  const key = `${index}_${type}`;
  
  const productImage = partInfo?.ProductImage ?? '';
  const productName = partInfo?.name ?? 'N/A';
  const purchaseLink = partInfo?.purchase_link ?? '#';

  return (
    <div>
      <img src={productImage} alt={productName} width="50" height="50"/>
      <span>{name}: {productName}</span>
      <button onClick={() => toggleMoreInfo(index, type)}>More Info</button>
      <a href={purchaseLink} target="_blank" rel="noopener noreferrer">Purchase</a>
      {showMoreInfo && showMoreInfo[key] ? (
        <div style={{ marginTop: '10px' }}>
          {Object.keys(partInfo ?? {}).map((infoKey, i) => (
            infoKey !== 'ProductImage' && infoKey !== 'purchase_link' && infoKey !== 'name' && infoKey !== 'id' ? 
              <span key={i} style={{ marginRight: '15px', display: 'block' }}>
                {infoKey}: {formatPart(infoKey, partInfo[infoKey])}
              </span> 
              : null
          ))}
        </div>
      ) : null}
    </div>
  );
};

export default PcHardware;
