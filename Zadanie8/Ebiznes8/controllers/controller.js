const User = require("../models/user");
const crypto = require('crypto');



const controller = {
    addNewUser: async function(req, res, next) {
        try {
            let {login, password} = req.body;
            login = calculateMD5(login);
            password = calculateMD5(password)
            const newUser = await User.create({
                login,
                password
            });
            res.status(201).json(newUser);
        } catch (error) {
            next(error);
        }
    },
    checkCredentials: async function(req, res, next) {
        try {
            let {login, password} = req.body;
            login = calculateMD5(login);
            password = calculateMD5(password)
            let user = await User.findOne({ where: {login} });
            if (!user) {
                res.render('index', { title: 'Login', message: 'User does not exist' });
            }
            else if (user.password !== password) {
                res.render('index', { title: 'Login', message: 'Incorrect password' });
            }
            else {
                res.cookie("logged", user);
                res.render('logged');
            }
        }
        catch (error) {
            next(error);
    }
    },

    logOut: async function(req, res, next) {
       try {
           res.clearCookie('logged');
           res.render('logout');
       }
           catch (error) {
               next(error)
            }
    }

};

function calculateMD5(input) {
    const hash = crypto.createHash('md5');
    hash.update(input);
    return hash.digest('hex');}

module.exports = controller;