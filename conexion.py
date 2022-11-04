import pymysql
from pymysql import MySQLError

class Conexion:

    def __init__(self):
        pass

    def __openConnection(self):
        try:
            self.__connection = pymysql.connect(
                host='localhost',
                user='root',
                password='',
                db='sithome'
            )
            self.__cursor = self.__connection.cursor()
            return True
        except MySQLError:
            print(MySQLError)
            return False

    def __closeConnection(self):
        try:
            self.__connection.close()
            return True
        except MySQLError:
            print(MySQLError)
            return False

    # def createDB(self, database_name):
    #     if self.__openConnection(database_name) == True:
    #         try:
    #             self.__cursor.execute(
    #                 'create table if not exists contactos(id integer PRIMARY KEY AUTOINCREMENT, name text, cel text, tel text, address text, city text)')
    #             self.__connection.commit()
    #             return True
    #         except MySQLError:
    #             print(MySQLError)
    #             return False
    #         finally:
    #             self.__closeConnection()
    #     else:
    #         return False

    def insert(self, sql):
        if self.__openConnection():
            try:
                self.__cursor.execute(sql)
                self.__connection.commit()
                return True
            except MySQLError:
                print(MySQLError)
                return False
            finally:
                self.__closeConnection()
        else:
            return False

    def select(self, sql):
        usuario = tuple()
        if self.__openConnection():
            try:
                self.__cursor.execute(sql)
                usuario = self.__cursor.fetchone()
                return usuario
            except MySQLError:
                print(MySQLError)
                return usuario
            finally:
                self.__closeConnection()
        else:
            return usuario

    def selectAll(self, sql):
        usuarios = tuple()
        if self.__openConnection():
            try:
                self.__cursor.execute(sql)
                usuarios = self.__cursor.fetchall()
                return usuarios
            except MySQLError:
                print(MySQLError)
                return usuarios
            finally:
                self.__closeConnection()
        else:
            return usuarios

    def update(self, sql):
        if self.__openConnection():
            try:
                self.__cursor.execute(sql)
                self.__connection.commit()
                return True
            except MySQLError:
                print(MySQLError)
                return False
            finally:
                self.__closeConnection()
        else:
            return False

    def delete(self, sql):
        if self.__openConnection():
            try:
                self.__cursor.execute(sql)
                self.__connection.commit()
                return True
            except MySQLError:
                print(MySQLError)
                return False
            finally:
                self.__closeConnection()
        else:
            return False