import mysql.connector

connect = mysql.connector.connect(host='localhost', user='root',password='123456',database='123')
connect.close()