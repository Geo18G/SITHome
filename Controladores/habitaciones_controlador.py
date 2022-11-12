from Modelos.habitacion_modelo import HabitacionModelo
from conexion import Conexion

class HabitacionControlador:
    def __init__(self):
        self.__conexion = Conexion()

    def crearHabitacion(self,habitacion):
        sql = f"INSERT INTO habitaciones (idhabitaciones, nombre) " \
              f"VALUES (NULL, '{habitacion.getNombreH()}')"
        return self.__conexion.insert(sql)


    def actualizarHabitacion(self,habitacion,id):
        sql = f"UPDATE habitaciones SET nombre ='{habitacion.getNombreH()}'" \
              f" WHERE idhabitaciones = '{id}'"
        return self.__conexion.update(sql)

    def eliminarHabitacion(self,id):
        sql = f"DELETE FROM habitaciones WHERE idhabitaciones = '{id}'"
        return self.__conexion.delete(sql)

    def obtener_ids(self):
        sql = f"SELECT idhabitaciones FROM habitaciones"
        retorno = self.__conexion.selectAll(sql)
        listaIds = list()
        for i in retorno:
            for j in i:
                listaIds.append(j)
        return listaIds

    def mostrarHabitacion(self,idU,idH):
        sql = f"SELECT h.* FROM habitaciones h INNER JOIN permisos p ON h.idhabitaciones = p.habitaciones_idhabitaciones  INNER JOIN  usuarios u ON u.idusuarios = p.usuarios_idusuarios " \
              f"WHERE p.usuarios_idusuarios = '{idU}' AND p.habitaciones_idhabitaciones = '{idH}' AND p.permiso = 1"
        return self.__conexion.select(sql)

    def idHabitacionEspecifica(self, nombre):
        sql = f"SELECT idhabitaciones FROM habitaciones WHERE nombre = '{nombre}'"
        return self.__conexion.select(sql)

#
# prueba = HabitacionControlador()
# # habitacion = HabitacionModelo()
# # # # habitacion.setNombreH("sala")
# # # # prueba.crearHabitacion(habitacion)
# # # # print(prueba.mostrarHabitacion())
# # # # habitacion.setNombreH("cocina")
# # # # prueba.actualizarHabitacion(habitacion,1)
# # # print(prueba.mostrarHabitacion())
# # # # # prueba.eliminarHabitacion(1)
# print(prueba.mostrarHabitacion(5,1))
