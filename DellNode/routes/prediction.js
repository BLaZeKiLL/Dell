let express = require('express');
let router = express.Router();

let {PythonShell} = require('python-shell');
const SCRIPT_PATH = 'D:/Projects/Dell/python';

router.post('/local', (req, res) => {
    let options = {
        mode: 'text',
        pythonOptions: ['-u'], // get print results in real-time
        scriptPath: SCRIPT_PATH,
        args: [req.body.code, req.body.quater]
    };

    PythonShell.run('localForecast.py', options, function(err, result) {
        if (err) console.log(err);
        res.json({ values: JSON.parse(result[0]), recom: JSON.parse(result[1]) });
    });

});

router.post('/global', (req, res) => {
    let options = {
        mode: 'text',
        pythonOptions: ['-u'], // get print results in real-time
        scriptPath: SCRIPT_PATH,
        args: [req.body.quater]
    };

    PythonShell.run('globalForecast.py', options, function(err, result) {
        if (err) console.log(err);
        res.json({ value: JSON.parse(result) });
    });
});

module.exports = router;