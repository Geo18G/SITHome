from Modelos.usuario_modelo import UsuarioModelo

from conexion import Conexion

class UsuarioControlador:
    def __init__(self):
        self.__conexion = Conexion()

    def crearUsuario(self,usuario):
        sql = f"INSERT INTO usuarios (idusuarios, nombre, contrasena, roles_idroles) " \
              f"VALUES (NULL, '{usuario.getNombreU()}','{usuario.getContrasenaU()}','{int(usuario.getRolU())}')"
        return self.__conexion.insert(sql)

    def actualizarUsuario(self, usuario, id):
        sql = f"UPDATE usuarios SET nombre='{usuario.getNombreU()}', contrasena='{usuario.getContrasenaU()}'," \
              f"roles_idroles='{usuario.getRolU()}' WHERE idusuarios= '{id}'"
        return self.__conexion.update(sql)

    def eliminarUsuario(self,id):
        sql = f"DELETE FROM usuarios WHERE idusuarios = '{id}'"
        return self.__conexion.delete(sql)

    def mostrarUsuario(self):
        sql = 'SELECT u.idusuarios, u.nombre, r.tipo  FROM usuarios u INNER JOIN  roles r on u.roles_idroles = r.idroles'
        registred_users = list()
        users = self.__conexion.selectAll(sql)
        for user in users:
            name = user[1]
            typpe = user[2]
            registred_users.append((f'{name}', f'{typpe}'))
        return registred_users


    def buscarUsuario(self, code):
        sql = f"SELECT * FROM usuarios WHERE contrasena = '{code}'"
        return self.__conexion.select(sql)

# prueba = UsuarioControlador()
# usuario = UsuarioModelo()
# usuario.setNombreU("Nacho")
# usuario.setcontrasena(123)
# usuario.setRolU(1)
# # prueba.crearUsuario(usuario)
# print(prueba.mostrarUsuario())
# # prueba.eliminarUsuario(2)
# prueba.actualizarUsuario(usuario,1)
# print(prueba.mostrarUsuario())

