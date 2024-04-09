const express = require('express');
const router = express.Router();

module.exports = function(handlePayment) {
    router.post('/', (req, res) => {
        const { paymentId, value } = req.body;
        handlePayment({ paymentId, value });
        res.json({ paymentId, value });
    });

    return router;
};
