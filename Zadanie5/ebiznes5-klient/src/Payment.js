import React from 'react';

function Payment({paymentId, setPaymentId, paymentValue, setPaymentValue, handlePayment}) {
    return (
        <div>
            <h2>Make Payment</h2>
            <label>
                Enter Payment ID:
                <input
                    type="text"
                    value={paymentId}
                    onChange={e => setPaymentId(e.target.value)}
                />
            </label>
            <label>
                Enter Payment Value:
                <input
                    type="text"
                    value={paymentValue}
                    onChange={e => setPaymentValue(e.target.value)}
                />
            </label>
            <button onClick={handlePayment}>Pay</button>
        </div>
    );
}

export default Payment;