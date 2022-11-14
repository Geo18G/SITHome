from conexion import Conexion


class PermisosControlador:
    def __init__(self):
        self.__conexion = Conexion()

    def crearPermisos(self,permiso):
        sql = f"INSERT INTO permisos (usuarios_idusuarios,habitaciones_idhabitaciones,permiso) " \
              f"VALUES ('{permiso.getIdUsuarioP()}','{permiso.getIdHabitacionP()}','{permiso.getPermiso()}')"
        return self.__conexion.insert(sql)

    def actualizarPermisos(self, idU, idH, permiso):
        sql = f"UPDATE permisos SET permiso ='{permiso}'" \
              f" WHERE usuarios_idusuarios = '{idU}' AND  habitaciones_idhabitaciones = '{idH}'"
        return self.__conexion.update(sql)

    def eliminarPermisos(self,idU, idH):
        sql = f"DELETE FROM permisos WHERE usuarios_idusuarios = '{idU}' AND  habitaciones_idhabitaciones = '{idH}'"
        return self.__conexion.delete(sql)

    def eliminarPermisosPorHab(self, idH):
        sql = f"DELETE FROM permisos WHERE  habitaciones_idhabitaciones = '{idH}'"
        return self.__conexion.delete(sql)

    def eliminarPermisosPorUs(self, idU):
        sql = f"DELETE FROM permisos WHERE  usuarios_idusuarios= '{idU}'"
        return self.__conexion.delete(sql)


    def mostrarPermisos(self):
        sql = f"SELECT * FROM permisos"
        return self.__conexion.selectAll(sql)

    def nuevoUsuarioPermisos(self, nombreU, idH):
        pass