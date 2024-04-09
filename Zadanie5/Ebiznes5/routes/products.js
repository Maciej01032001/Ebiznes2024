const express = require('express');
const router = express.Router();

module.exports = function(products) {
    router.get('/', (req, res) => {
        res.json(products);
    });

    return router;
};