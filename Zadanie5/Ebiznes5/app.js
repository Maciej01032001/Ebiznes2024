const createError = require('http-errors');
const express = require('express');
const path = require('path');
const cookieParser = require('cookie-parser');
const logger = require('morgan');
const cors = require('cors');
const bodyParser = require('body-parser');
const app = express();

app.use(bodyParser.json());
app.use(cors());

const products = [
    {id: 1, name: 'Krzeslo', price: 100},
    {id: 2, name: 'Stol', price: 2000},
    {id: 3, name: 'Fotel', price: 300}
];

function handlePayment(paymentData) {
    console.log('Otrzymano dane platnosci:');
    console.log(paymentData);
}

const indexRouter = require('./routes/index');
const productsRouter = require('./routes/products')(products);
const paymentRouter = require('./routes/payment')(handlePayment);


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


module.exports = app;
