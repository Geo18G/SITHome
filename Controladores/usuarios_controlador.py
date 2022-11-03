from Modelos.usuario_modelo import UsuarioModelo
import pymysql
from conexion import Conexion

class UsuarioControlador:
    conexion = Conexion()

    def crearUsuario(self,usuario):
        sql = f"INSERT INTO usuarios (idusuarios, nombre, contrasena, roles_idroles) " \
              f"VALUES (NULL, '{usuario.getNombreU()}','{usuario.getContrasenaU()}','{int(usuario.getRolU())}')"
        try:
            self.conexion.cursor.execute(sql)
            self.conexion.connection.commit()
            print("usuario ingresado")

        except:
            print("no se puede ingresar usuario")

    def actualizarUsuario(self):
        pass

    def eliminarUsuario(self):
        pass

    def mostrarUsuario(self):
        sql = 'SELECT nombre, roles_idroles FROM usuarios'

        try:
            registred_users = list()
            self.conexion.cursor.execute(sql)
            users = self.conexion.cursor.fetchall()
            for user in users:
                name = user[0]
                typpe = user[1]
                registred_users.append((f'{name}', f'{typpe}'))
            return registred_users
        except:
            print("error all users")

    def buscarUsuario(self, code):
        sql = f"SELECT * FROM usuarios WHERE contrasena = '{code}'"
        try:
            self.conexion.cursor.execute(sql)
            print(1)
            usuario = self.conexion.cursor.fetchone()
            return usuario
        except:
            print("error, usuario no encontrado")
            return False

