import React, { useState, useEffect } from 'react';
import { LandingPage } from './pages/LandingPage';

function App() {
  const [data, setData] = useState({'name': "hi"})

  // useEffect(() => {
  //   fetch("/userDetails").then(
  //     res => res.json()
  //   ).then(
  //     data => {
  //       setData(data)
  //       console.log(data)
  //     }
  //   )
  // }, [])

  return (
    <div>
      <LandingPage />
      {/* {(typeof data.name !== "string") ? (
        <p>Loading...</p>
      ): (<h1>{data.name}</h1>
      )} */}

    </div>
  );
}

export default App;
