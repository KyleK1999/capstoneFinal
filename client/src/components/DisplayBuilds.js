import React, { useEffect, useState } from 'react';

function DisplayBuilds(props) {
  const [builds, setBuilds] = useState([]);

  useEffect(() => {
    const urlParams = new URLSearchParams(window.location.search);
    const minPrice = urlParams.get('minPrice');
    const maxPrice = urlParams.get('maxPrice');

    // Fetch builds based on minPrice and maxPrice
    fetch(`http://localhost:5555/get_builds?minPrice=${minPrice}&maxPrice=${maxPrice}`)
      .then(response => response.json())
      .then(data => {
        setBuilds(data.builds);
      })
      .catch(error => console.error('Error:', error));
  }, []);

  return (
    <div>
      <h2>Builds</h2>
      <ul>
        {builds.map((build, index) => (
          <li key={index}>
            {/* Display build details here. Replace with your own structure */}
            Build ID: {build.id}, Price Range ID: {build.price_range_id}, Build Type ID: {build.build_type_id}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default DisplayBuilds;
