import pyodbc

server = 'DELLWARE'  # Replace with your server name if different
database = 'Customers'  # Replace with your database name

# # Establish the database connection using Windows Authentication
# connection_string = f'DRIVER=SQL Server;
# SERVER={server};
# DATABASE={database};
# Trusted_Connection=yes;"
connection = pyodbc.connect(
    "DRIVER={SQL Server};"
    "SERVER=DELLWARE;"
    "DATABASE=ABCE;"
    "Trusted_Connection=yes;"
)

# Create a cursor to execute SQL queries
cursor = connection.cursor()

# Query 1: Retrieve first two rows
query1 = 'SELECT TOP 2 CustomerID, FirstName, LastName FROM Customers'
cursor.execute(query1)
for row in cursor:
    print(row)

print('\n')

# Query 2: Retrieve customers with specific registration date
query2 = '''
    SELECT CustomerID,
    CONCAT(FirstName, ' ', LastName) AS FullName,
    RegistrationDate
    FROM Customers
    WHERE RegistrationDate >= '2023-01-01'
    ORDER BY RegistrationDate DESC
'''
cursor.execute(query2)
for row in cursor:
    print(row)

# Close the cursor and connection
cursor.close()
connection.close()
