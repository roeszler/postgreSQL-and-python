"""
Import Modules
"""
import psycopg2


# ---------- Connect to "Chinook" database
connection = psycopg2.connect(database="chinook")

# ---------- Build a cursor object of the database
# ---------- a 'set' or 'list', similar to an 'array' in JavaScript
cursor = connection.cursor()


# # ---------- Query 1 - select all records from the "Artist" table
# cursor.execute('SELECT * FROM "Artist"')  # psycopg2 command syntax
# # ---------- SELECT * FROM "Artist"; ------ SQL DB syntax

# # ---------- Query 2 - select only the "Name" column from the "Artist" table
# cursor.execute('SELECT "Name" FROM "Artist"')

# # ---------- Query 3 - select only "Queen" from the "Artist" table
# cursor.execute('SELECT * FROM "Artist" WHERE "Name" = %s', ["Queen"])

# # ---------- Query 4 - select only by PK "ArtistId" #51 from the "Artist" table
# cursor.execute('SELECT * FROM "Artist" WHERE "ArtistId" = %s', [51])

# # ---------- Query 5 - select only the albums with "ArtistId" #51 on the "Album" table
# cursor.execute('SELECT * FROM "Album" WHERE "ArtistId" = %s', [51])

# ---------- Query 6 - select all tracks where the composer is "Queen" from the "Track" table
cursor.execute('SELECT * FROM "Track" WHERE "Composer" = %s', ["Queen"])

# # ---------- Test 1 - select all tracks where the composer is "Black Sabbath" from the "Track" table
# cursor.execute('SELECT * FROM "Track" WHERE "Composer" = %s', ["Black Sabbath"])

# # ---------- Test 1 - select all tracks where the composer is "Test" from the "Track" table
# cursor.execute('SELECT * FROM "Track" WHERE "Composer" = %s', ["Test"])

# ---------- Fetch the results (multiple) from the cursor as tuple
results = cursor.fetchall()

# ---------- Fetch the results (single) from the cursor as column
# results = cursor.fetchone()

# ---------- Close the connection
connection.close()

# ---------- Iterate out each value and print the results
for result in results:
    print(result)
