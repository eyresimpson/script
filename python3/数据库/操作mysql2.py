import mysql.connector

# Connect to the database
conn = mysql.connector.connect(
    host="hostname",
    user="username",
    password="password",
    database="database_name"
)

# Create a cursor object
cursor = conn.cursor()

# Execute a SELECT query
query = "SELECT * FROM table_name"
cursor.execute(query)

# Fetch all the rows of a query result
rows = cursor.fetchall()
for row in rows:
    print(row)

# Close the cursor and connection
cursor.close()
conn.close()
