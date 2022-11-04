from Modelos.usuario_modelo import UsuarioModelo
import pymysql
from conexion import Conexion

class UsuarioControlador:
    def __init__(self):
        self.__conexion = Conexion()

    def crearUsuario(self,usuario):
        sql = f"INSERT INTO usuarios (idusuarios, nombre, contrasena, roles_idroles) " \
              f"VALUES (NULL, '{usuario.getNombreU()}','{usuario.getContrasenaU()}','{int(usuario.getRolU())}')"
        return self.__conexion.insert(sql)

    def actualizarUsuario(self, usuario, id):
        sql = f"UPDATE usuarios SET nombre='{usuario.getNombreU()}', contrasena='{usuario.getContrasena()}'," \
              f"roles_idroles='{usuario.getRolU()}' WHERE idusurios={id}"
        return self.__conexion.update(sql)

    def eliminarUsuario(self,id):
        sql = f"DELETE FROM usuarios WHERE idusuarios = '{id}'"
        return self.__conexion.delete(sql)

    def mostrarUsuario(self):
        sql = 'SELECT nombre, roles_idroles FROM usuarios'
        registred_users = list()
        users = self.__conexion.selectAll(sql)
        for user in users:
            name = user[0]
            typpe = user[1]
            registred_users.append((f'{name}', f'{typpe}'))
        return registred_users


    def buscarUsuario(self, code):
        sql = f"SELECT * FROM usuarios WHERE contrasena = '{code}'"
        return self.__conexion.select(sql)



