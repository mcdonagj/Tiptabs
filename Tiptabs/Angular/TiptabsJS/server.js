var express = require('express');
var app = express();

app.use(express.static("TiptabsJS"));
app.get('/', function (req, res, next) {
    res.sendFile('/Users/mcdonagj/Desktop/Schoolwork/Projects/Python/Tiptabs/Tiptabs/Angular/TiptabsJS/index.html');
});
app.listen(8080, 'localhost');