import React, { useEffect, useRef } from 'react';
import Chart from 'chart.js/auto';

const ComponentChart = ({ componentName, sortKey }) => {
  const chartRef = useRef(null);

  const fetchData = async () => {
    try {
      const response = await fetch('http://localhost:3000/chart');
      const allData = await response.json();
      const data = allData[`${componentName.toLowerCase()}_data`];
      const sortedData = [...data].sort((a, b) => a[sortKey] - b[sortKey]);

      const primaryDataset = {
        label: sortKey,
        data: sortedData.map(item => item[sortKey]),
        yAxisID: 'y-axis-1',
        backgroundColor: 'rgba(75, 192, 192, 0.2)',
        borderColor: 'rgba(75, 192, 192, 1)',
        borderWidth: 1,
      };

      const secondaryDataset = {
        label: 'Price',
        data: sortedData.map(item => item.Price),
        yAxisID: 'y-axis-2',
        backgroundColor: 'rgba(255, 99, 132, 0.2)',
        borderColor: 'rgba(255, 99, 132, 1)',
        borderWidth: 1,
      };

      const datasets = [primaryDataset];
      if (sortKey !== 'Price') {
        datasets.push(secondaryDataset);
      }

      const ctx = chartRef.current.getContext('2d');
      new Chart(ctx, {
        type: 'bar',
        data: {
          labels: sortedData.map(item => item.name),
          datasets: datasets,
        },
        options: {
          scales: {
            'y-axis-1': {
              beginAtZero: true,
              position: 'left',
            },
            'y-axis-2': {
              beginAtZero: true,
              position: 'right',
            },
          },
        },
      });
    } catch (error) {
      console.error(`Error fetching data for ${componentName}:`, error);
    }
  };

  useEffect(() => {
    fetchData();
  }, [componentName, sortKey]);

  return (
    <div>
      <h1>{componentName} Chart</h1>
      <canvas ref={chartRef} width="400" height="400"></canvas>
    </div>
  );
};

export default ComponentChart;
