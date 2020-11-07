var express = require('express');
var mongoose = require('mongoose');
var cors = require('cors');
var bodyparser = require('body-parser');
var mallController = require('./Controller/mallController');

var app = express();
var port = 3000;

app.use(cors());
app.use(bodyparser.json());
app.use(bodyparser.urlencoded({ extended: false }));

mongoose.connect("mongodb://localhost:27017/mallDatabase",{ useUnifiedTopology: true, useNewUrlParser: true });

const connection = mongoose.connection;

connection.once("open", function() {
  console.log("MongoDB database connection established successfully");
});


app.get('/', (req,res) => {
    res.send("Welcome to Navigation api");
});

app.use('/api', mallController)

app.listen(port, () => {
  console.log("Server started at port: " + port);
});