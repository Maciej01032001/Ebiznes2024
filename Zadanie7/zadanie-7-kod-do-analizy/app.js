const createError = require('http-errors');
const express = require('express');
const path = require('path');
const cookieParser = require('cookie-parser');
const logger = require('morgan');
const cors = require('cors');
const app = express();

app.use(cors());

const products = [
    {id: 1, name: 'Krzeslo', price: 100},
    {id: 2, name: 'Stol', price: 2000},
    {id: 3, name: 'Fotel', price: 300}
];

function handlePayment(paymentData) {
    console.log("Payment data acquired:");
    console.log(paymentData);
}

const indexRouter = require('./routes/index');
const productsRouter = require('./routes/products')(products);
const paymentRouter = require('./routes/payments')(handlePayment);


app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'ejs');


app.use(logger('dev'));
app.use(express.json());
app.use(express.urlencoded({extended: false}));
app.use(cookieParser());
app.use(express.static(path.join(__dirname, 'public')));

app.use('/', indexRouter);
app.use('/products', productsRouter);
app.use('/payment', paymentRouter);

app.use(function (req, res, next) {
    next(createError(404));
});

app.use(function(err, req, res) {
    console.error(err.stack);
    res.status(500).send('Something broke!');
});


module.exports = app;
