import React, {useState, useEffect} from 'react';
import {BrowserRouter as Router, Routes, Route, Link} from 'react-router-dom';
import Products from './Products';
import Payment from './Payment';
import Basket from './Basket';

function App() {
    const [products, setProducts] = useState([]);
    const [paymentId, setPaymentId] = useState('');
    const [paymentValue, setPaymentValue] = useState('');
    const [productsInBasket, setProductsInBasket] = useState([]);

    useEffect(() => {
        handleProducts();
    }, []);

    const handleProducts = async () => {
        try {
            const response = await fetch('https://ebiznes10serwer.azurewebsites.net/products');
            const data = await response.json();
            setProducts(data);
        } catch (error) {
            console.error('Error:', error);
        }
    };

    const handlePayment = async () => {
        try {
            const response = await fetch('https://ebiznes10serwer.azurewebsites.net/payment', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    paymentId: paymentId,
                    value: paymentValue,
                }),
            });
            if (response.ok) {
                console.log('Payment OK');
            } else {
                console.error('Payment FAIL');
            }
        } catch (error) {
            console.error('Error:', error);
        }
    };

    return (
        <Router>
            <div>
                <nav>
                    <ul>
                        <li>
                            <Link to="/">Go to Products</Link>
                        </li>
                        <li>
                            <Link to="/payment">Go to Payment</Link>
                        </li>
                        <li>
                            <Link to="/basket">Go to Basket</Link>
                        </li>
                    </ul>
                </nav>

                <Routes>
                    <Route path="/payment" element={<Payment
                        paymentId={paymentId}
                        setPaymentId={setPaymentId}
                        paymentValue={paymentValue}
                        setPaymentValue={setPaymentValue}
                        handlePayment={handlePayment}
                    />}/>
                    <Route path="/basket" element={<Basket productsInBasket={productsInBasket}/>}/>
                    <Route path="/"
                           element={<Products products={products} setProductsInBasket={setProductsInBasket}/>}/>
                </Routes>
            </div>
        </Router>
    );
}

export default App;

