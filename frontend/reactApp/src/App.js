import React, { useState } from 'react';
import logo from './logo.svg';
import './App.css';

function App() {
  const [data, setData] = useState(null);
  const [error, setError] = useState(null); // Add this line

  const fetchData = async () => {
    try {
      const response = await fetch('http://127.0.0.1:5051/api/data');
      if (!response.ok) { // if HTTP-status is 404, 500 or other not 2xx, the catch block will trigger
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      const data = await response.json(); // This parses the data from JSON to a JavaScript object
      setData(data.data);
      setError(null); // Reset the error message upon successful fetch
    } catch (error) {
      setError('Fetching data failed'); // Set the error message when the fetch fails
    }
  };

  return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <button onClick={fetchData}>
            Fetch data
          </button>

          {/* Show data fetched from server or error message */}
          {error ? <p>{error}</p> : <p>{data}</p>}

        </header>
      </div>
  );
}

export default App;