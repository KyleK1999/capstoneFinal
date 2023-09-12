import React from 'react';
import { BrowserRouter as Router, Route, Redirect } from 'react-router-dom';
import Login from './components/Login';
import SelectPriceRange from './components/SelectedPriceRange';
import DisplayBuilds from './components/DisplayBuilds'; 

function App() {
  return (
    <Router>
      <Route path="/login" exact component={Login} />
      <Route path="/select_price_range" exact component={SelectPriceRange} />
      <Route path="/display-builds" exact component={DisplayBuilds} /> 
      <Route path="/" exact>
        <Redirect to="/login" />
      </Route>
    </Router>
  );
}

export default App;
