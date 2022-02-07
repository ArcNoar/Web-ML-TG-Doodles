import psycopg2

from .conf import db_name,host,user,password

def sql_connector():
    try:
        connection = psycopg2.connect(
    
            host = host,
            user = user,
            password = password,
            database = db_name
            )
    
        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT version();"
                )
            print(f'Server version : {cursor.fetchone()}')

    
    except Exception as _ex:
        print('Ошибка в ходе чтения ДБ', _ex)
    
    finally:
        if connection:
            connection.close()
            print('Дб отключена')