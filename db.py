import pypyodbc

with open(".pw") as f:
  password = f.read()

def createDB():  
    connection = connection = pypyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
                                            'Server=137.135.135.105;'
                                            'Database=master;'
                                            'encrypt=yes;'
                                            'TrustServerCertificate=yes;'
                                            'UID=sa;'
                                            'PWD=' + password, autocommit=True)

    cursor = connection.cursor()
    SQLCommand = ("CREATE DATABASE IF NOT EXISTS user_data;")
    cursor.execute(SQLCommand)
    SQLCommand = ("CREATE TABLE users(user_id INT AUTO_INCREMENT,name VARCHAR(255) NOT NULL,email VARCHAR(255) NOT NULL,password VARCHAR(255) NOT NULL,PRIMARY KEY(user_id);")
    cursor.execute(SQLCommand)
    print('done')

