import React from 'react';
import { useHistory } from 'react-router-dom'; // Importing useHistory

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
      alert('Please login first.');
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
      alert(data.message);
      history.push(`/display-builds?minPrice=${minPrice}&maxPrice=${maxPrice}`);  // Redirecting here
    })
    .catch(err => {
      console.error("Failed to set price range:", err);
    });
  };

  return (
    <div>
      <h1>Select Price Range</h1>
      <button onClick={() => handlePriceRangeSelection(500, 750)}>500 - 750</button>
      <button onClick={() => handlePriceRangeSelection(751, 1000)}>751 - 1000</button>
      <button onClick={() => handlePriceRangeSelection(1001, 1500)}>1001 - 1500</button>
    </div>
  );
}

export default SelectPriceRange;
