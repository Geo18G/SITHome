from conexion import Conexion


class DispositivosControlador:
    def __init__(self):
        self.__conexion = Conexion()

    def crearDispositivos(self,permiso):
        sql = f"INSERT INTO permisos (usuarios_idusuarios,habitaciones_idhabitaciones,permiso) " \
              f"VALUES ('{permiso.getIdUsuarioP()}','{permiso.getIdHabitacionP()}','{permiso.getPermiso()}')"
        return self.__conexion.insert(sql)

    def actualizarDispositivos(self,permiso, idU, idH):
        sql = f"UPDATE habitaciones SET permiso ='{permiso.getPermiso()}'" \
              f" WHERE usuarios_idusuarios = '{idU}' AND  habitaciones_idhabitaciones = '{idH}'"
        return self.__conexion.update(sql)

    def eliminarDispositivos(self,idU, idH):
        sql = f"DELETE FROM dispositivos WHERE usuarios_idusuarios = '{idU}' AND  habitaciones_idhabitaciones = '{idH}'"
        return self.__conexion.delete(sql)

    def mostrarDispositivos(self):
        sql = f"SELECT * FROM permisos"
        return self.__conexion.selectAll(sql)
