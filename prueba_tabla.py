# from PyQt5 import QtWidgets, uic
#
#
# app = QtWidgets.QApplication([])
#
# tabla = uic.loadUi("prueba_tabla.ui")
#
# users = list()
#
# fila = 0
#
# users.append(('geo', 'admin'))
# users.append(('nacho', 'admin'))
# users.append(('martin', 'usuario'))
# for registro in users:
#     columna = 0
#     tabla.user_table.insertRow(fila)
#     for elemento in registro:
#         celda = QtWidgets.QTableWidgetItem(elemento)
#         tabla.user_table.setItem(fila, columna, celda)
#         columna+=1
#     fila+=1
#
# tabla.user_table.setItem(3, 0, QtWidgets.QTableWidgetItem('elemento'))
# btn1 = tabla.boton
# tabla.user_table.setCellWidget(3, 0, btn1)
# tabla.show()
# app.exec()
from passlib.context import CryptContext

contexto = CryptContext(
    schemes=["pbkdf2_sha256"],
    default="pbkdf2_sha256",
    pbkdf2_sha256_default_rounds=3000
)
texto = "123"
texto_encriptado = contexto.hash(texto)
print(texto_encriptado)
