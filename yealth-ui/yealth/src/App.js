import React, { Component } from 'react';
import logo from './logo.svg';
import styles from './App.css';

import { render } from 'react-dom';
import FlatButton from 'material-ui/FlatButton';
import Toolbar from 'material-ui/Toolbar';


function App() {
  return (
    <Toolbar>
      <FlatButton color='black' Label='Hello World'>
        Lat Long map
    </FlatButton>
    <FlatButton color='black' Label='Hello World'>
        Heatmap
    </FlatButton>
    </Toolbar>
  );
}

export default App;
