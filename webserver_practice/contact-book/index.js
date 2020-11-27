// index.js

var express = require('express');
var mongoose = require('mongoose');
var app = express();

// DB setting
mongoose.set('useNewUrlParser', true);
mongoose.set('useFindAndModify', false);
mongoose.set('useCreateIndex', true);
mongoose.set('useUnifiedTopology', true);

mongoose.connect(process.env.MONGO_DB);     // process.env : 환경변수
var db = mongoose.connection;

db.once('open', function() {
    console.log('DB connected');
});

db.on('error', function() {
    console.log('DB ERROR : ', err);
});

// Other settings
app.set('view engine', 'ejs');
app.use(express.static(__dirname + '/public'));

// Port setting
var port = 3001;
app.listen(port, function() {
    console.log('server on! http://localhost:' + port);
});