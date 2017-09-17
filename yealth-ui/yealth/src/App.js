import React, { Component } from 'react';
import logo from './logo.svg';
import styles from './App.css';

import { render } from 'react-dom';
import FlatButton from 'material-ui/FlatButton';
import Toolbar from 'material-ui/Toolbar';

const newStyle = {
  
};


function App() {
  return (
    <Toolbar style={styles.toolbar_style}>
      <FlatButton color='black' Label='Hello World'>
        Lat Long map
    </FlatButton>
    <FlatButton color='black' Label='Hello World'>
        Heatmap
    </FlatButton>
    </Toolbar>
  );
}

render(<App />, document.querySelector('#titlebar'));

export default App;
