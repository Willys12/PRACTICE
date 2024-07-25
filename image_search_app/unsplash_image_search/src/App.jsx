// eslint-disable-next-line no-unused-vars
import axios from 'axios';
// eslint-disable-next-line no-unused-vars
import React, { useEffect, useRef, useState, useCallback } from 'react';
import { Button, Form } from 'react-bootstrap';
import './index.css';

const API_URL = 'https://api.unsplash.com/search/photos';
const IMAGES_PER_PAGE = 20;

function App() {
  const searchInput = useRef(null);
  const [images, setImages] = useState([]);
  const [totalPages, setTotalPages] = useState(0);
  const [page, setPage] = useState(1);
  const [errorMsg, setErrorMsg] = useState("");

  const fetchImages = useCallback(async () => {
    try {
      if (searchInput.current.value) {
        setErrorMsg('');
        const {data} = await axios.get(
          `${API_URL}?query=${
            searchInput.current.value
          }&page=${page}&per_page=${IMAGES_PER_PAGE}&client_id=${
            import.meta.env.VITE_API_KEY
          }`
        );
        setImages(data.results);
        setTotalPages(data.total_pages);
      }
    } catch (error) {
      setErrorMsg("Error fetching your image. Try agin ater");
      console.log(error);
    } 
  }, [page]);

  useEffect(() => {
    fetchImages();
  }, [fetchImages, page]);

  const resetSearch = () => {
    setPage(1);
    fetchImages();
  }
  const handleSearch = (event) => {
    event.preventDefault();
    console.log(searchInput.current.value);
    resetSearch();
  };

  const handleSelection = (selection) => {
    searchInput.current.value = selection;
    resetSearch();
  }
  console.log('page', page);
  return (
    <>
      <div className='container'>
        <h1 className='title'>Image Search</h1>
        {errorMsg && <p className='error-msg'>{errorMsg}</p>}
        <div className="search-section">
        <form onSubmit={handleSearch}>
        <Form.Control
        type="search"
        placeholder="Type something to search"
        className='search-input'
        ref={searchInput}
        />
        </form>
        </div>
        <div className="filters">
          <div onClick={() => handleSelection('Nature')}>Nature</div>
          <div onClick={() => handleSelection('Bird')}>Bird</div>
          <div onClick={() => handleSelection('Cats')}>Cats</div>
          <div onClick={() => handleSelection('Shoes')}>Shoes</div>
        </div>
        <div className="images">
          {images.map((image) => {
            return (
            <img 
            key={image.id}
            src={image.urls.small}
            alt={image.alt_description}
            className='image'
            />
            );
          })}
        </div>
        <div className="buttons">
          {page > 1 && (
            <Button onClick={() => setPage(page - 1)}>Previous</Button>)}
          {page < totalPages && (
            <Button onClick={() => setPage(page + 1)}>Next</Button>)}
        </div>        
      </div>
    </>
  );
}

export default App;
