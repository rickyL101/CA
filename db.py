#https://stackoverflow.com/questions/8932261/create-mysqldb-database-using-python-script/25621844

import mysql.connector

with open(".pw") as f:
    password = f.read()

#establish connection to remote database
connection = mysql.connector.connect(host="remotemysql.com", user="Doc0XDVVtG", password="" + password, database="Doc0XDVVtG")
cursor = connection.cursor()
#create the table(s) required 

def createDB():
    cursor.execute("create table IF NOT EXISTS users(user_id INT NOT NULL AUTO_INCREMENT,name varchar(100) NOT NULL,email varchar(100) NOT NULL,password varchar(100) NOT NULL,PRIMARY KEY(user_id));")


