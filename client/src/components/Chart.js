import React, { useEffect, useState } from 'react';
import ComponentChart from './ComponentChart';

const MyChart = () => {
  const [data, setData] = useState({
    cpu_data: null,
    gpu_data: null,
    memory_data: null,
    motherboard_data: null,
    storage_data: null,
    psu_data: null,
  });

  const fetchData = async () => {
    try {
      const response = await fetch('http://localhost:3000/chart');
      const chartData = await response.json();
            setData(chartData);
    } catch (error) {
      console.error('Error fetching data:', error);
    }
  };

  useEffect(() => {
    fetchData();
  }, []);

  return (
    <div>
      <h1>Charted Data For All Components</h1>
      {data.cpu_data && <ComponentChart componentName="CPU" componentData={data.cpu_data} sortKey="Speed" />}
      {data.gpu_data && <ComponentChart componentName="GPU" componentData={data.gpu_data} sortKey="Speed" />}
      {data.memory_data && <ComponentChart componentName="Memory" componentData={data.memory_data} sortKey="Speed" />}
      {data.motherboard_data && <ComponentChart componentName="MotherBoard" componentData={data.motherboard_data} sortKey="Price" />}
      {data.storage_data && <ComponentChart componentName="Storage" componentData={data.storage_data} sortKey="Size" />}
      {data.psu_data && <ComponentChart componentName="PSU" componentData={data.psu_data} sortKey="Wattage" />}
    </div>
  );
};

export default MyChart;
