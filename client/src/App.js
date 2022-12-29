import './App.css';
import { useState } from 'react'

function App() {
  const [area, setArea] = useState('')
  const [location, setLocation] = useState('')
  const [bath, setBath] = useState(0)
  const [bhk, setBhk] = useState(0)
  const [price, setPrice] = useState('')

  const getEstimatedPrice = () => 
  {
    // var url = 'http://127.0.0.1:5000/predict_home_price';
    const data = {
      total_sqft : parseFloat(area),
      bhk : bhk,
      bath: bath,
      location:location
    }
    fetch('http://127.0.0.1:5000/predict_home_price', {
      method: "POST", 
      body: JSON.stringify(data),
      headers: {
        "Content-Type": "application/json"
      }
    } , {mode: 'cors'})
    .then((res) => res.json())
    .then((data) => {
      console.log(data)
      setPrice(data.estimated_price)
    });

  }

  return (
    <div className="App">
      <header className="App-header">
        <form>
          <div className='flex flex-col'>
            <label>
              Area(in sqft)
            </label>
            <input type="text" name="area"
              onChange={e => setArea(e.target.value)}
            />
          </div>
          <div className='flex flex-col'>
            <label>
              Location
            </label>
            <input type="text" name="location"
              onChange={e => setLocation(e.target.value)}
            />
          </div>
          <div className='flex flex-col'>
            <label>
              Bathrooms
            </label>
            <input type="text" name="bath"
              onChange={e => setBath(e.target.value)}
            />
          </div>
          <div className='flex flex-col'>
            <label>
              Bedrooms
            </label>
            <input type="text" name="bhk"
              onChange={e => setBhk(e.target.value)}
            />
          </div>
          
        </form>
        <button className="Button" name='Submit' value="Submit" onClick={()=>{getEstimatedPrice()}}/>
        <div><label>
          Estimated Price - {price}
        </label>
        </div>
      </header>
    </div>
  );
}

export default App;
