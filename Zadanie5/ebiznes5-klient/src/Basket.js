import React from 'react';

function Basket({productsInBasket}) {
    return (
        <div>
            <h1>Basket contains:</h1>
            <ul>
                {productsInBasket.map(product => (
                    <li key={product.id}>{product.name}</li>
                ))}
            </ul>
        </div>
    );
}

export default Basket;