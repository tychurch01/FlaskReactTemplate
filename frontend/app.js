import React, { useEffect, useState } from 'react';

function App() {
  const [data, setData] = useState(null)

  useEffect(() => {
    fetch('/api/data')
        .then(response => response.json())
        .then(data => setData(data));
  }, []);

  return (
    <div className="App">
      <h1>React App</h1>
      <pre>{JSON.stringify(data, null, 2)}</pre>
    </div>
  );
}

export default App;