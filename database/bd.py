import mysql.connector
import app.database.datos as datos

class Database:
    _connection = None

    @classmethod
    def conectar(cls):
        if cls._connection is None:
            try:
                cls._connection = mysql.connector.connect(**datos.credenciales)
            except mysql.connector.Error as e:
                print("Error al conectar a la base de datos: ", e)
                return None        
        return cls._connection

    @classmethod
    def execute_query(cls, query, params=None):
        connection = cls.conectar()
        if connection is None:
            return None
        cursor = connection.cursor()
        try:
            cursor.execute(query, params)
            connection.commit()
        except mysql.connector.Error as e:
            print("Error al ejecutar la consulta: ", e)
        finally:
            cursor.close()
        return cursor.rowcount

    @classmethod
    def fetch_one(cls, query, params=None):
        cursor = cls.execute_query(query, params)
        if cursor:
            return cursor.fetchone()
        else:
            return None
        

    @classmethod
    def fetch_all(cls, query, params=None):
        cursor = cls.execute_query(query, params)
        if cursor:
            return cursor.fetchall()
        else:
            return None

    @classmethod
    def closeConn(cls):
        if cls._connection is not None:
            cls._connection.close()
            cls._connection = None


