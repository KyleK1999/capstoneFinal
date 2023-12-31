import React from 'react';
import { BrowserRouter as Router, Route, Redirect, Switch, useHistory } from 'react-router-dom';
import { ToastContainer } from 'react-toastify'; 
import Login from './components/Login';
import SelectPriceRange from './components/SelectedPriceRange';
import DisplayBuilds from './components/DisplayBuilds';
import UserProfile from './components/UserProfile';
import Navbar from './components/NavBar';
import Chart from './components/Chart';



function App() {
  const history = useHistory();
  const currentPath = history.location.pathname;
  const noNavbarRoutes = ['/login'];

  return (
    <Router>
      <ToastContainer />  
      <Navbar currentPath={currentPath} noNavbarRoutes={noNavbarRoutes} />
      <Switch>
        <Route path="/login" exact component={Login} />
        <Route path="/select_price_range" exact component={SelectPriceRange} />
        <Route path="/display-builds" exact component={DisplayBuilds} />
        <Route path="/profile" exact component={UserProfile} />
        <Route path="/chart" exact component={Chart} /> 
        <Redirect to="/login" />
      </Switch>
    </Router>
  );
}

export default App;
