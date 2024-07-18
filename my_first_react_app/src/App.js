import React, { useState } from 'react';


const ExampleComponent = () => {
  // Initialize the state variable 'data' with empty string ("") and provide setData to update it
  const [data, setData] = useState("");

  // Function to handle input change and update state.
  const handleChange = (event) => {
    setData(event.target.value);
  };

  return (
    <>
    <div>
      <input type='text' value={data} onChange={handleChange} />
      <p>The current value is: {data}</p>
    </div>
    </>
  );
};

export default ExampleComponent;
