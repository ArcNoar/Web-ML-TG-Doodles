import psycopg2

from .conf import db_name,host,user,password
#from Web.Asiya.models import Person_Memory

def sql_connector(): # Бесполезный Класс, так как вписывать все сюда, это дичь ебаная, буду создавать отдельные класс, с вызовом.
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


"""
Нужно сделать связующую дб фукцию для каждого табла.
Социальная Память:
    Person_Memory
    Возможно нам не пригодится писать триллиард дб, если мне сейчас удастся прикрутить сюда джангу

    
"""
#class PM_Sql(Person_Memory):
    
    
