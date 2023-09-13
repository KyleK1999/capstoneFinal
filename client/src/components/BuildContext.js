import React, { createContext, useContext, useState } from 'react';

const BuildContext = createContext();

export const useBuild = () => {
  return useContext(BuildContext);
};

export const BuildProvider = ({ children }) => {
  const [builds, setBuilds] = useState([]);

  const switchPart = (newBuilds) => {
    setBuilds(newBuilds);
  };

  return (
    <BuildContext.Provider value={{ builds, switchPart }}>
      {children}
    </BuildContext.Provider>
  );
};