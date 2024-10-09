import pymysql

def get_connection():
    return pymysql.connect(
        host='localhost',
        user='tiago',
        password='Jimi2022',
        database='movie'
    )

