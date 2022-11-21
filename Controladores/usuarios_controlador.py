from conexion import Conexion

class UsuarioControlador:
    def __init__(self):
        self.__conexion = Conexion()

    def crearUsuario(self,usuario):
        sql = f"INSERT INTO usuarios (idusuarios, nombreUsuario, contrasena, roles_idroles) " \
              f"VALUES (NULL, '{usuario.getNombreU()}','{usuario.getContrasenaU()}','{usuario.getRolU()}')"
        return self.__conexion.insert(sql)

    def actualizarUsuario(self, usuario, id):
        sql = f"UPDATE usuarios SET nombreUsuario='{usuario.getNombreU()}', contrasena='{usuario.getContrasenaU()}'," \
              f"roles_idroles='{usuario.getRolU()}' WHERE idusuarios = '{id}'"
        return self.__conexion.update(sql)

    def eliminarUsuario(self,id):
        sql = f"DELETE FROM usuarios WHERE idusuarios = '{id}'"
        return self.__conexion.delete(sql)

    def mostrarUsuario(self):
        sql = 'SELECT u.idusuarios, u.nombreUsuario, r.tipo  FROM usuarios u INNER JOIN  roles r on u.roles_idroles = r.idroles'
        return self.__conexion.selectAll(sql)


    def buscarUsuario(self, nombre):
        sql = f"SELECT u.idusuarios, u.nombreUsuario, r.tipo, u.contrasena FROM usuarios u INNER JOIN  roles r on u.roles_idroles = r.idroles WHERE u.nombreUsuario = '{nombre}'"
        return self.__conexion.select(sql)


