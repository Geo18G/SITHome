from Modelos.usuario_modelo import UsuarioModelo

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
        sql = 'SELECT u.idusuarios, u.nombreUsuario, u.contrasena, r.tipo  FROM usuarios u INNER JOIN  roles r on u.roles_idroles = r.idroles'
        registred_users = list()
        users = self.__conexion.selectAll(sql)
        for user in users:
            id = user[0]
            name = user[1]
            typpe = user[3]
            registred_users.append((f'{id}', f'{name}', f'{typpe}'))
        return registred_users

    def obtener_ids(self):
        sql = f"SELECT idusuarios FROM usuarios"
        retorno = self.__conexion.selectAll(sql)
        listaIds = list()
        for i in retorno:
            for j in i:
                listaIds.append(j)
        return listaIds

    def buscarUsuario(self, nombre, contrasena):
        sql = f"SELECT * FROM usuarios WHERE contrasena = '{contrasena}' AND nombreUsuario = '{nombre}'"
        return self.__conexion.select(sql)

# prueba = UsuarioControlador()
# usuario = UsuarioModelo()
# usuario.setNombreU("Geo")
# usuario.setContrasenaU(111)
# usuario.setRolU(1)
# # prueba.crearUsuario(usuario)
# #print(prueba.mostrarUsuario())
# # prueba.eliminarUsuario(3)
# prueba.actualizarUsuario(usuario,1)
# print(prueba.mostrarUsuario())

