let express = require('express');
let bodyParser = require('body-parser');
let cors = require('cors');
let app = express();

/**
 * Express setup
 */
app.use(cors());
/**
 * Body-Parser setup
 */
app.use(bodyParser.urlencoded({extended: true, defer: true}));
app.use(bodyParser.text());                                   
app.use(bodyParser.json({ type: 'application/json'})); 

/**
 * Frontend Modules exports
 */
app.use(express.static(__dirname + "/public"));

/**
 * Routes setup
 */
let data = require('./routes/data');
let prediction = require('./routes/prediction');
let service = require('./routes/service');

app.use('/data', data);
app.use('/prediction', prediction);
app.use('/service', service);

app.listen(3000, () => {
    console.log("Serving on http://localhost:3000/");
});