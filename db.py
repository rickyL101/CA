import pypyodbc

with open(".pw") as f:
  password = f.read()

connection = connection = pypyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
                                           'Server=137.135.135.105;'
                                           'Database=master;'
                                           'encrypt=yes;'
                                           'TrustServerCertificate=yes;'
                                           'UID=sa;'
                                           'PWD=' + password, autocommit=True)

cursor = connection.cursor()
def createDB():  
    SQLCommand = ("IF EXISTS(SELECT name FROM master.dbo.sysdatabases WHERE name = N'userData')BEGIN SELECT 'Database Name already Exist' AS Message END ELSE BEGIN CREATE DATABASE [userData] SELECT 'New Database is Created' END;")
    cursor.execute(SQLCommand) 
    SQLCommand = ("IF NOT EXISTS (SELECT 1 FROM INFORMATION_SCHEMA.TABLES T WHERE T.TABLE_SCHEMA = 'dbo' AND T.TABLE_NAME = 'users') BEGIN CREATE TABLE dbo.users(user_id INT IDENTITY(1, 1),name VARCHAR(255) NOT NULL,email VARCHAR(255) NOT NULL,password VARCHAR(255) NOT NULL,PRIMARY KEY(user_id)) END;")
    cursor.execute(SQLCommand)
    print('done')



