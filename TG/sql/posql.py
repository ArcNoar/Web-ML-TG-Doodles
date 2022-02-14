import psycopg2

from .conf import db_name,host,user,password
#from Web.Asiya.models import Person_Memory
#unic_id,first_name,sur_name,birthday,gender

def sql_connector(): # Бесполезный Класс, так как вписывать все сюда, это дичь ебаная, буду создавать отдельные класс, с вызовом.
    try:
        connection = psycopg2.connect(
    
            host = host,
            user = user,
            password = password,
            database = db_name
            )
    
        cursor = connection.cursor()
        insert_query = """ INSERT INTO "Asiya_person_memory" (unic_id, first_name, sur_name,gender) VALUES
                                          ('000000223', 'Ноев', 'Мудак','Male')"""
        cursor.execute(insert_query)
        connection.commit()
                
    
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
#class PM_Sql:
    
    
