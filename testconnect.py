import psycopg2

connection = psycopg2.connect(
    user = 'postgres',
    password = 'admin',
    host = '127.0.0.1',
    port = '5432',
    database = 'tk_app_db'
)
print(connection)

try:
    with connection:
        with connection.cursor() as cursor:
            query = "select * from users where name=%s and passwd=%s"
            values = ('natalia', ,)
            cursor.execute(query, values)
            registers = cursor.rowcount
            print(registers)
except Exception as e:
    print("Ocurrio un error: {}".format(e))
finally:
    connection.close()