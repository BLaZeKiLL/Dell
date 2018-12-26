let express = require('express');
let router = express.Router();

let {PythonShell} = require('python-shell');
const SCRIPT_PATH = 'D:/Projects/Dell/python';

router.get('/globalAnalysis', (req, res) => {
    let options = {
        mode: 'text',
        pythonOptions: ['-u'], // get print results in real-time
        scriptPath: SCRIPT_PATH,
        args: ["global"]
    };

    PythonShell.run('GetSalesData_node.py', options, function(err, result) {
        if (err) console.log(err);
        res.json(JSON.parse(result));
    });
});

router.get('/globalSales', (req, res) => {

    let options = {
        mode: 'text',
        pythonOptions: ['-u'], // get print results in real-time
        scriptPath: SCRIPT_PATH,
    };

    PythonShell.run('globalPredictions.py', options, function(err, result) {
        if (err) console.log(err);
        res.json(JSON.parse(result));
    });
});

router.get('/localAnalysis', (req, res) => {
    let options = {
        mode: 'text',
        pythonOptions: ['-u'], // get print results in real-time
        scriptPath: SCRIPT_PATH,
        args: ["region"]
    };

    PythonShell.run('GetSalesData_node.py', options, function(err, result) {
        if (err) console.log(err);
        res.json(JSON.parse(result)[req.query.region]);
    });
});

router.get('/localSales', (req, res) => {
    let options = {
        mode: 'text',
        pythonOptions: ['-u'], // get print results in real-time
        scriptPath: SCRIPT_PATH,
        args: [req.query.region]
    };

    PythonShell.run('localPredictions.py', options, function(err, result) {
        if (err) console.log(err);
        res.json(JSON.parse(result));
    });
});

router.get('/localGeneration', (req, res) => {
    let options = {
        mode: 'text',
        pythonOptions: ['-u'], // get print results in real-time
        scriptPath: SCRIPT_PATH,
        args: ["generation"]
    };

    PythonShell.run('GetSalesData_node.py', options, function(err, result) {
        if (err) console.log(err);
        res.json(JSON.parse(result)[req.query.region]);
    });
});

router.get('/globalGenerations', (req, res) => {
    let options = {
        mode: 'text',
        pythonOptions: ['-u'], // get print results in real-time
        scriptPath: SCRIPT_PATH,
        args: ["global_generation"]
    };

    PythonShell.run('GetSalesData_node.py', options, function(err, result) {
        if (err) console.log(err);
        res.json(JSON.parse(result));
    });
});

router.get('/localOccupations', (req, res) => {
    let options = {
        mode: 'text',
        pythonOptions: ['-u'], // get print results in real-time
        scriptPath: SCRIPT_PATH,
        args: ["occupation"]
    };

    PythonShell.run('GetSalesData_node.py', options, function(err, result) {
        if (err) console.log(err);
        res.json(JSON.parse(result)[req.query.region]);
    });
});

router.get('/globalOccupations', (req, res) => {
    let options = {
        mode: 'text',
        pythonOptions: ['-u'], // get print results in real-time
        scriptPath: SCRIPT_PATH,
        args: ["global_occupation"]
    };

    PythonShell.run('GetSalesData_node.py', options, function(err, result) {
        if (err) console.log(err);
        res.json(JSON.parse(result));
    });
});

module.exports = router;