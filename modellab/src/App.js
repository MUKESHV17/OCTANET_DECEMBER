import React, { useEffect, useState } from 'react';
import axios from 'axios';

function App() {
    const [products, setProducts] = useState([]);
    const [cart, setCart] = useState([]);

    useEffect(() => {
        axios.get('http://127.0.0.1:8000/products/')
            .then(response => setProducts(response.data))
            .catch(error => console.error(error));
    }, []);

    const addToCart = (product) => {
        setCart([...cart, product]);
    };

    return (
        <div className="container mt-4">
            <h1>Simple E-commerce Store</h1>
            <h2>Cart: {cart.length} items</h2>
            <div className="row">
                {products.map(product => (
                    <div className="col-md-4" key={product.id}>
                        <div className="card">
                            <img src={product.image} className="card-img-top" alt={product.name} />
                            <div className="card-body">
                                <h5 className="card-title">{product.name}</h5>
                                <p className="card-text">{product.description}</p>
                                <p className="card-text">₹{product.price}</p>
                                <button onClick={() => addToCart(product)} className="btn btn-primary">
                                    Add to Cart
                                </button>
                            </div>
                        </div>
                    </div>
                ))}
            </div>
        </div>
    );
}

export default App;
