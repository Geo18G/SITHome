from conexion import Conexion

class RolControlador:
    def __init__(self):
        self.__conexion = Conexion()

    def crearRol(self,rol):
        sql = f"INSERT INTO roles (idroles, tipo) " \
              f"VALUES (NULL, '{rol.getTipoR()}')"
        return self.__conexion.insert(sql)

    def actualizarRol(self, rol, id):
        sql = f"UPDATE roles SET tipo ='{rol.getTipoR()}'" \
              f" WHERE idroles = '{id}'"
        return self.__conexion.update(sql)

    def eliminarRol(self, id):
        sql = f"DELETE FROM roles WHERE idroles = '{id}'"
        return self.__conexion.delete(sql)

    def mostrarRol(self):
        sql = f"SELECT * FROM roles"
        return self.__conexion.selectAll(sql)

