import os, psycopg2

def get_connection():
    url = os.environ['DATABASE_URL']
    connection = psycopg2.connect(url)
    return connection

def get_all_library():
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute(sql)
    
    sql = 'SELECT title, author, publisher, isbn, type FROM books_Python'
    
    cursor.execute(sql)
    rows = cursor.fetchall()
        
    cursor.close()
    connection.close()
    
    return rows

def select_library(titles):
    connection = get_connection()
    cursor = connection.cursor()
    sql = "SELECT * FROM books_python  WHERE title LIKE %s OR author LIKE %s"
    cursor.execute(sql, ('%' + titles + '%', '%' + titles + '%'))
    connection.commit()
    rows = cursor.fetchall()
    cursor.close()
    connection.close()
    return rows

def insert_library(title ,author,publisher, isbn):
    connection = get_connection()
    cursor = connection.cursor()
    sql = 'INSERT INTO books_python VALUES (defalut, %s, %s, %s, %s)'
    cursor.execute(sql,(title,author,publisher,isbn))
    connection.commit()
    
    cursor.close()
    connection.close()
    
    
    