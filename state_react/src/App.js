import './App.css';
import React from 'react';
import ReactDOM from'react-dom/client';

class App extends React.Component {
  constructor (props) {
    super(props);
    this.state = {
      date: new Date()
    };
  }
  componentDidMount () {
    this.timerID = setInterval(
      () => this.tick(),
      1000
    );
  }
  componentWillUnmount () {
    clearInterval(this.timerID);
  }
  tick() {
    this.setState({date: new Date()});
  }
  render () {
    return (
      <div>
        <h1>Hello, World</h1>
        <h2>The time is{this.state.date.toLocaleTimeString()}</h2>
      </div>
    );
  }
}

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(<App />);

export default App;
