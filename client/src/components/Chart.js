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
    <div className="container mt-4">
      <h1 className="text-center mb-4">Charted Data For All Components</h1>
      <div className="row">
        {data.cpu_data && <div className="col-lg-6"><ComponentChart componentName="CPU" componentData={data.cpu_data} sortKey="Speed" /></div>}
        {data.gpu_data && <div className="col-lg-6"><ComponentChart componentName="GPU" componentData={data.gpu_data} sortKey="Speed" /></div>}
        {data.memory_data && <div className="col-lg-6"><ComponentChart componentName="Memory" componentData={data.memory_data} sortKey="Speed" /></div>}
        {data.motherboard_data && <div className="col-lg-6"><ComponentChart componentName="MotherBoard" componentData={data.motherboard_data} sortKey="Price" /></div>}
        {data.storage_data && <div className="col-lg-6"><ComponentChart componentName="Storage" componentData={data.storage_data} sortKey="Size" /></div>}
        {data.psu_data && <div className="col-lg-6"><ComponentChart componentName="PSU" componentData={data.psu_data} sortKey="Wattage" /></div>}
      </div>
    </div>
  );
};

export default MyChart;
