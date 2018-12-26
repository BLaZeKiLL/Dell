let express = require('express');
let router = express.Router();

let {PythonShell} = require('python-shell');
const SCRIPT_PATH = 'D:/Projects/Dell/python';

router.get('/local', (req, res) => {
    let options = {
        mode: 'text',
        pythonOptions: ['-u'], // get print results in real-time
        scriptPath: SCRIPT_PATH,
    };

    PythonShell.run('services.py', options, function(err, result) {
        if (err) console.log(err);
        res.json({ main: JSON.parse(result[1])[req.query.code], prob: JSON.parse(result[0])[req.query.code] });
    });
});

module.exports = router;