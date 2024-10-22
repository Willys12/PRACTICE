import React, { useState } from 'react';
import { calculatePAYE } from './actions/payeActions';
import { useDispatch, useSelector } from 'react-redux';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faFacebook, faTwitter, faLinkedin } from '@fortawesome/free-brands-svg-icons';
import './App.css';

function App() {
  const [salary, setSalary] = useState('');
  const dispatch = useDispatch();
  const deductions = useSelector(state => state.deductions);

  const handleSubmit = (event) => {
    event.preventDefault();
    dispatch(calculatePAYE(parseFloat(salary)));
  };

  return (
    <div className='App'>
      <header> PAYE Calculator Logo</header>
      <div className='container'>
        <form onSubmit={handleSubmit}>
          <label htmlFor='grossSalary'>Enter Gross Salary</label>
          <input 
          type='number'
          id='grossSalary'
          value={salary}
          onChange={e => setSalary(e.target.value)}
          required
          />
          <button type='submit'>Calculate</button>
        </form>
        <div id="result">
            <p><strong>PAYE:</strong> Ksh {deductions.paye.toFixed(2)}</p>
            <p><strong>NSSF:</strong> Ksh {deductions.nssf.toFixed(2)}</p>
            <p><strong>NHIF:</strong> Ksh {deductions.nhif.toFixed(2)}</p>
            <p><strong>Housing Levy:</strong> Ksh {deductions.housingLevy.toFixed(2)}</p>
            <p><strong>Total Deductions:</strong> Ksh {deductions.totalDeductions.toFixed(2)}</p>
            <p><strong>Net Salary:</strong> Ksh {deductions.netSalary.toFixed(2)}</p>
        </div>
        
      </div>
      <footer>
          <p>Connect with us on:</p>
          <ul>
            <li><a href='https://www.facebook.com/home'><FontAwesomeIcon icon={faFacebook} className='fa-icon' /></a></li>
            <li><a href='https://x.com/home'><FontAwesomeIcon icon={faTwitter} className='fa-icon' /></a></li>
            <li><a href='https://www.linkedin.com/feed/'><FontAwesomeIcon icon={faLinkedin} className='fa-icon' /></a></li>
          </ul>
          <p>&copy; 2024 Kenya PAYE Calc.</p>
        </footer>
    </div>
  );
}

export default App;
