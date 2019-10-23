let ejs = require('ejs');
let express = require('express'); 
let bodyParser = require('body-parser');
let app = express();

app.set('view engine', 'ejs');

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({   
    extended: true
})); 
app.use(express.json());       
app.use(express.urlencoded());

app.get('/', (req, res) => {
    res.render('index');
});

app.post('/', (req, res) => {
    res.render('result',{ name: req.body.name, email: req.body.email, address: req.body.address });
});

app.listen(3000, () => console.log('Example app listening on port 3000!'));