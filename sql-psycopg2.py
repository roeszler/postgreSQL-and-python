"""
Import Modules
"""
import psycopg2


# ---------- Connect to "Chinook" database
connection = psycopg2.connect(database="chinook")

# ---------- Build a cursor object of the database
# ---------- a 'set' or 'list', similar to an 'array' in JavaScript
cursor = connection.cursor()

# ---------- Query 1 - select all records from the "Artist" table
cursor.execute('SELECT * FROM "Artist"')

# ---------- Fetch the results (multiple) from the cursor
results = cursor.fetchall()

# ---------- Fetch the results (single) from the cursor
# results = cursor.fetchone()

# ---------- Close the connection
connection.close()

# ---------- Iterate out each value and print the results
for result in results:
    print(result)
