import React from 'react';
import { useHistory } from 'react-router-dom';
import { toast } from 'react-toastify';

function getCookie(name) {
  const value = `; ${document.cookie}`;
  const parts = value.split(`; ${name}=`);
  if (parts.length === 2) return parts.pop().split(';').shift();
}

function SelectPriceRange() {
  const history = useHistory();

  const handlePriceRangeSelection = (minPrice, maxPrice) => {
    const username = getCookie('username');

    if (!username) {
      toast.error('Please login first.');  
      return;
    }

    fetch('http://localhost:5555/set_price_range', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        username,
        selected_price_range: { min_price: minPrice, max_price: maxPrice },
      }),
    })
    .then(res => res.json())
    .then(data => {
      toast(data.message);  
      history.push(`/display-builds?minPrice=${minPrice}&maxPrice=${maxPrice}`);  
    })
    .catch(err => {
      toast.error("Failed to set price range");  
      console.error("Failed to set price range:", err);
    });
  };

  return (
    <div className="container mt-5">
      <div className="row justify-content-center">
        <div className="col-md-4">
          <h1 className="text-center mb-4">Select Price Range</h1>
          <div className="d-grid gap-2">
            <button 
              className="btn btn-primary" 
              onClick={() => handlePriceRangeSelection(500, 750)}
            >
              500 - 750
            </button>
            <button 
              className="btn btn-secondary" 
              onClick={() => handlePriceRangeSelection(751, 1000)}
            >
              751 - 1000
            </button>
            <button 
              className="btn btn-success" 
              onClick={() => handlePriceRangeSelection(1001, 1500)}
            >
              1001 - 1500
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}

export default SelectPriceRange;
