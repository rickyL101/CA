import pypyodbc

with open(.pw) as f:
    password = f.read()

def createDB():
    
        
    connection = connection = pypyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
                                            'Server=137.135.135.105;;'
                                            'Database=master;'
                                            'encrypt=yes;'
                                            'TrustServerCertificate=yes;'
                                            'UID=sa;'
                                            'PWD=' + password, autocommit=True)

    cursor = connection.cursor()
    SQLCommand = ("CREATE DATABASE userData;")
    cursor.execute(SQLCommand)
    print('done')

