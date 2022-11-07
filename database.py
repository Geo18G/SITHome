import pymysql

class Database:
    # def __init__(self):
    #     self.connection = pymysql.connect(
    #         host='localhost',
    #         user='root',
    #         password='',
    #         db='sithome'
    #     )
    #
    #     self.cursor = self.connection.cursor()
    #     print("conexion correcta")

    def select_code(self, code):
        sql = f"SELECT * FROM users WHERE code = '{code}'"
        try:
            self.cursor.execute(sql)
            user = self.cursor.fetchone()
            return user
        except:
            print("error, usuario no encontrado")
            return False

    def is_admin(self, code):
        sql = f"SELECT type FROM users WHERE type = 'Administrador' AND code = '{code}'"

        try:
            self.cursor.execute(sql)
            user = self.cursor.fetchone()
            typpe = user[0]
            return typpe
        except:
            return "Usuario"

    def select_all_users(self):
        sql = 'SELECT name, type FROM users'

        try:    
            registred_users = list()
            self.cursor.execute(sql)
            users = self.cursor.fetchall()
            for user in users:
                name = user[0]
                typpe = user[1]
                registred_users.append((f'{name}', f'{typpe}'))
            return registred_users
        except:
            print("error all users")
    
    def uptade_user(self, id, code):
        sql = f"UPDATE users SET code='{code}'WHERE id={id}"

        try:
            self.cursor.execute(sql)
            self.connection.commit()
        except:
            print("ERROR IN UPTATE")
    
    def insert_user(self, name, code, type):
        sql= f"INSERT INTO users (id, name, code, type) VALUES (NULL, '{name}', '{code}', '{type}')"

        try:
            self.cursor.execute(sql)
            self.connection.commit()
            print("usuario ingresado")
            
        except:
            print("no se puede ingresar usuario")

    def checkStatusDB(self, device):
        sql = f"SELECT status FROM devices WHERE name = '{device}'"

        try:
            self.cursor.execute(sql)
            status = self.cursor.fetchone()
            status = status[0]
            return status
        except:
            print("no se reconoce el dispositivo")
    
    def changeStatusDB(self, device):
        status = database.checkStatusDB(device)
        if status == 'ON':
            sql = (f"UPDATE devices SET status = 'OFF' WHERE name = '{device}'")
            try:
                self.cursor.execute(sql)
                self.connection.commit()
            except:
                print("No se pudo actualizar el status")
        elif status == 'OFF':
            sql = (f"UPDATE devices SET status = 'ON' WHERE name = '{device}'")
            try:
                self.cursor.execute(sql)
                self.connection.commit()
            except:
                print("No se pudo actualizar el status")

    def close(self):
        self.connection.close()
        print("conexion a base de datos cerrada")

# database = Database()
# database.changeStatusDB("Luz")
