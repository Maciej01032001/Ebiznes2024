import React from 'react';

function Products({products, setProductsInBasket}) {
    const addToBasket = (product) => {
        setProductsInBasket(prevBasket => [...prevBasket, product]);
    };

    return (
        <div>
            <h1>Products list:</h1>
            <ul>
                {products.map(product => (
                    <li key={product.id}>
                        {product.name}
                        <button onClick={() => addToBasket(product)}>Add to Basket</button>
                    </li>
                ))}
            </ul>
        </div>
    );
}

export default Products;
