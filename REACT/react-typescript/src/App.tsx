import React, {Component} from 'react'
import logo from './logo.svg';
import './App.css';
import Message from './Message';

class App extends Component {
  render() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <Message/>
      </header>
    </div>
  );
  }
}

export default App;
