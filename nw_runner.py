import pyodbc

# Let's establish the connection using PYODBC
server = "18.135.103.95"
database = "Northwind"
username = "SA"
password = "Passw0rd2018"
connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                                  'SERVER='+server+';DATABASE='+database+';UID=' + username + ';PWD=' + password)

cursor = connection.cursor()
cursor.execute("CREATE TABLE Beth_table")

