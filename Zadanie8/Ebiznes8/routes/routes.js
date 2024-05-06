const express = require('express');
const router = express.Router();
const controller = require('../controllers/controller');

router.get('/', function(req, res) {
  if(!req.cookies.logged) {
    res.render('index', {title: 'Login', message: ''});
  }
  else {
    res.render('logged');
  }
});

router.get('/register', function(req, res) {
  res.render('register', { title: 'Register', message: '' });
});

router.post('/', controller.checkCredentials);

router.post('/register', controller.addNewUser);

router.post('/logout', controller.logOut);


module.exports = router;
