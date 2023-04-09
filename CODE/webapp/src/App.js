import React, { useState } from 'react';

import SearchBar from './components/SearchBar';
import Output from './components/Output';
import './App.css';
import './styles/style.css';
import './styles/card.scss';
const App = () => {
  // State to store the query value
  const [query, setQuery] = useState([]);

  // Function to update the query value
  const updateQuery = (req) => {
    setQuery(req);
  }

  return (
    <div>
      <div className='shell'>
        <div className="wrap">
          <div className="box" style={{ 'background': '#fff' }}>
            {/* Pass the updateQuery function to the SearchBar component */}
            <SearchBar updateQuery={updateQuery} />
          </div>
          {/* Pass the query value to the Output component */}
          <div className="box" style={{ 'background': '#ff5751' }}>
            <Output query={query}></Output>
          </div >
        </div >
      </div>

      {/* Footer with credits */}
      <div className="footer">Developed by Akash, Bhargav, Charles & Vansh</div>

    </div>
  );
};

export default App;