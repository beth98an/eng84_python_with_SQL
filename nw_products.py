# functionality
import pyodbc


class NwProducts:

    def __init__(self):
        self.server = "18.135.103.95"
        self.database = "Northwind"
        self.username = "SA"
        self.password = "Passw0rd2018"
        self.connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                                         'SERVER=' + self.server + ';DATABASE=' + self.database + ';UID=' + self.username + ';PWD=' + self.password)
        self.cursor = self.connection.cursor()

    def retrieve_all_data_from_products(self):
        prod_rows = self.cursor.execute("SELECT * FROM Products").fetchall()
        return prod_rows

    def create_table(self):
        try:
            return self.cursor.execute("SELECT * FROM beth").fetchall()
        except:
            self.cursor.execute("SELECT * INTO beth FROM Products")
        finally:
            return self.cursor.execute("SELECT * FROM beth").fetchall()

    def stock(self):
        table = self.cursor.execute("SELECT * FROM beth").fetchall()
        for item in table:
            return item
