import psycopg2
import sys

class Connection:
    _USERNAME = 'postgres'
    _PASSWORD = 'admin'
    _HOST = '127.0.0.1'
    _PORT = '5432'
    _DATABASE = 'tk_app_db'
    _connection = None
    _cursor = None
    
    @classmethod
    def getConnection(cls):
        
        if cls._connection is None:
            try:
                cls._connection = psycopg2.connect(
                    user = cls._USERNAME, 
                    password = cls._PASSWORD,
                    host = cls._HOST,
                    port = cls._PORT,
                    database = cls._DATABASE
                )
                print("Se realizo correctamente la conexion")
                return cls._connection

            except Exception as e:
                print("Ocurrio un error: {}".format(e))
                print(cls._USERNAME, cls._PASSWORD, cls._HOST, cls._PORT, cls._DATABASE)
                sys.exit()
                
        else:
            return cls._connection

    @classmethod
    def getCursor(cls):

        if cls._cursor is None:
            try:
                cls._cursor = cls.getConnection().cursor()
                print("El cursor se creo correctamente: {}".format(cls._cursor))
                return cls._cursor
            except Exception as e:
                print("Ocurrio un error: {}".format(e))
                sys.exit()
                  
        else: 
            return cls._cursor
        
if __name__ == "__main__": 
    Connection.getConnection()
    Connection.getCursor()