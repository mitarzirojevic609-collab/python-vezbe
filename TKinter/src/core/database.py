import pymysql


def connect_to_db():
    connection = pymysql.connect(
        host="localhost",
        user="root",
        passwd="12061998",
        database="book_keeping",
    )
    return connection