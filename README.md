# Python with SQL

## Apply CRUD
## Making data persistent

## Establishing a connection with PYODBC
- To establish connection between python and SQL we will use PYODBC
```
import pyodbc

# Let's establish the connection using PYODBC
server = "18.135.103.95"
database = "Northwind"
username = "xx"
password = "xxxxxxx"
docker_Northwind = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                                  'SERVER='+server+';DATABASE='+database+';UID=' + username + ';PWD=' + password)
```

- Checking if the connection has been validated and cursor object is created
```
cursor = docker_Northwind.cursor()
print(cursor. execute("SELECT @@version;"))
```
- Fetching some data from Northwind DB
```
row = cursor.fetchone()
print(row)

# Let's connect to our DB and fetch some data from customer
cust_rows = cursor.execute("SELECT * FROM Customers").fetchall()
print(cust_rows)
# We use execute to run our queries within a string
# fetchall() gets all the data from the table

prod_rows = cursor.execute("SELECT * FROM Products").fetchall()
# Let's iterate through the Product Table and check the UnitPrices available
for records in prod_rows:
    print(records.UnitPrice)

rows = cursor.execute("SELECT * FROM Products")
while True:
    record = rows.fetchone()
    if record is None:
        break
    print(record.UnitPrice)
```
### Useful links to help debug PYODBC installation
- For Windows
https://docs.microsoft.com/en-gb/sql/connect/odbc/download-odbc-driver-for-sql-server?view=sql-server-ver15

- for linux
https://packages.microsoft.com/ubuntu/20.04/prod/pool/main/m/msodbcsql17/
https://packages.microsoft.com/ubuntu/18.04/prod/pool/main/m/msodbcsql17/

## SQL Task
OOP example using pyodbc
Create an example of how we can create service objects related to a particular table.
An sql manager for the products table
create an object that relates only to the products table in the Northwind database. The reason for creating a single object for any table within the database would be to ensure that all functionality we build into this relates to what could be defined as a 'business function'.
As an example the products table, although relating to the rest of the company, will service a particular area of the business in this scenario we will simply call them the 'stock' department.
The stock department may have numerous requirements, and it makes sense to contain all the requirements a code actions within a single object.
Create two files nw_products.py & nw_runner.py, and then we will move into creating our object.
APPLY OOP - DRY CRUD WHERE POSSIBLE
