import mysql from 'mysql'

let conexion = mysql.createConnection({
    host: 'espun.cbuao0iqqnjm.us-east-1.rds.amazonaws.com',
    user: 'admin',
    password: '12345678',
    database: 'db_mile'
})

conexion.connect(function (error) {
    if (error) {
        console.log('Error de conexion a la base de datos');
    } else {
        console.log('Conexion a la base de datos exitosa');
    }
});

var InsertUsuario = function (nombre1, nombre2, apellido1, apellido2, usuario, clave) {
    conexion.query('INSERT INTO seg_usuarios (nombre1, nombre2, apellido1, apellido2, usuario, clave) VALUES (?,?,?,?,?,?)', [nombre1, nombre2, apellido1, apellido2, usuario, clave], function (error) {
        if (error) {
            console.log('Error al insertar el usuario' + error);
        } else {
            console.log('Usuario insertado correctamente');
        }
    });
}
export default InsertUsuario;