from Modelos.dispositivos_modelo import DispositivoModelo
from conexion import Conexion


class DispositivoControlador:
    def __init__(self):
        self.__conexion = Conexion()

    def crearDispositivo(self,dispositivo):
        sql = f"INSERT INTO dispositivos (iddispositivos, nombre, estado, habitaciones_idhabitaciones) " \
              f"VALUES (NULL, '{dispositivo.getNombreD()}','{dispositivo.getStatus()}','{dispositivo.getHabitacionD()}')"
        return self.__conexion.insert(sql)

    def actualizarDispositivo(self,dispositivo,id):
        sql = f"UPDATE dispositivos SET nombre ='{dispositivo.getNombreD()}',estado ='{dispositivo.getStatus()}'," \
              f"habitaciones_idhabitaciones ='{(dispositivo.getHabitacionD())}' WHERE iddispositivos = '{id}'"
        return self.__conexion.update(sql)

    def eliminarDispositivo(self,id):
        sql = f"DELETE FROM dispositivos WHERE iddispositivos = '{id}'"
        return self.__conexion.delete(sql)

    def mostrarDispositivos(self,idH):
        sql = f"SELECT nombre, estado FROM dispositivos WHERE habitaciones_idhabitaciones = '{idH}'"
        return self.__conexion.selectAll(sql)


# prueba = DispositivoControlador()
# disp = DispositivoModelo()
# # disp.setNombreD("foco")
# # disp.setStatusD(False)
# # disp.setHabitacionD(1)
# #
# # # prueba.crearDispositivo(disp)
# # # print(prueba.mostrarDispositivo())
# # # dispositivo.setNombreH("cocina")
# # # prueba.actualizarDispositivo(disp,2)
# # print(prueba.mostrarDispositivo())
# # prueba.eliminarDispositivo(2)
# print(prueba.mostrarDispositivo(1))
