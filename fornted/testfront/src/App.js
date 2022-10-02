import "./App.css";
import React, { useEffect, useState } from "react";
import axios from "axios";
function App() {
  const [data, setData] = useState([]);
  const [cities, setcities] = useState([]);
  const [city, setcity] = useState("");

  const getData = async () => {
    const res = await axios.get(`http://127.0.0.1:5000/customers/${city}`);
    setData(res.data);
    const resC = await axios.get(`http://127.0.0.1:5000/cities`);
    setcities(resC.data);
    // console.log(res.data);
  };

  useEffect(() => {
    getData();
  }, []);

  return (
    <div className="App">
      {data.map((customer) => (
        <div>
          name: {customer.name}, comp:{customer.comp}, title:{customer.title},
          city:{customer.city}
        </div>
      ))}
      City name:{" "}
      <select onChange={(e) => setcity(e.target.value)}>
        {cities.map((city) => (
          <option>{city.city}</option>
        ))}
      </select>
      <button onClick={() => getData()}>get city</button>
      {/* {JSON.stringify(cities)} */}
    </div>
  );
}

export default App;
