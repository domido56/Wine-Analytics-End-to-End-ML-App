import pyodbc

connection_str=(
    "Driver={ODBC Driver 17 for SQL Server};"
    "Server=.;"
    "Database=WineWarehouse;"
    "Trusted_Connection=yes;"    
)

try:
    connection = pyodbc.connect(connection_str)
    print("OK")
    connection.close()
except Exception as e:
    print(f"error: {e}")