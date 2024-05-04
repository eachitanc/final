import ex from 'express';
import dir from 'path';
import InsertUser from './base.js';

const app = ex();
const __dirname = dir.resolve();
app.use(ex.static('mile/build'));
app.use(ex.json());
app.use(ex.urlencoded({}));

app.listen(3000, function () {
    console.log('Server is running on port 3000');
});
app.get('/', function (req, res) {
    res.sendFile(__dirname + '/mile/index.html');
});

app.get('/usuarios', function (req, res) {
    res.sendFile(__dirname + '/mile/index.html');
});

app.get('/actividades', function (req, res) {
    res.sendFile(__dirname + '/mile/index.html');
});
app.post('/guardarUsuario', function (req, res) {
    var { nombre1, nombre2, apellido1, apellido2, usuario, clave } = req.body
    InsertUser(nombre1, nombre2, apellido1, apellido2, usuario, clave);
    res.send('Usuario guardado');
});