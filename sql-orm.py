"""
The reason that we no longer need to import the Table class, is because with the ORM,
we're not going to create tables, but instead, we'll be creating Python classes.
"""
from sqlalchemy import (
    create_engine, Column, Float, ForeignKey, Integer, String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# The Python classes that we'll create will subclass the declarative_base, meaning that
# any class we're making will extend from the main class within the ORM.

# Also instead of making a connection to the database directly, we'll be asking for a session

# ------------ Executing the instructions from the "chinook" database

# Use create_engine to point to our specific database location.
# This tells the application that we're using the Postgres server, on a local host since
# there are 3 slashes, in order to connect to our Chinook database:

db = create_engine("postgresql:///chinook")

# will grab the metadata that is produced by our database table schema (db), and 
# creates a subclass to map everything back to us here within the 'base' variable:

base = declarative_base()

# ------------ Class based models

# create a class-based model for the "Artist" table
class Artist(base):
    __tablename__ = "Artist"  # creates the table
    ArtistId = Column(Integer, primary_key=True) # identifies Primary Key
    Name = Column(String) # indicates sub-columns

# create a class-based model for the "Album" table
class Album(base):
    __tablename__ = "Album"
    AlbumId = Column(Integer, primary_key=True)
    Title = Column(String)
    ArtistId = Column(Integer, ForeignKey("Artist.ArtistId")) # points to the ArtistId in the Artist CBM

# create a class-based model for the "Track" table
class Track(base):
    __tablename__ = "Track"
    TrackId = Column(Integer, primary_key=True)
    Name = Column(String)
    AlbumId = Column(Integer, ForeignKey("Album.AlbumId"))
    MediaTypeId = Column(Integer, primary_key=False)
    GenreId = Column(Integer, primary_key=False)
    Composer = Column(String)
    Milliseconds = Column(Integer, primary_key=False)
    Bytes = Column(Integer, primary_key=False)
    UnitPrice = Column(Float)


# ------------ Create the session for the database to be accessed

# Instead of connecting to the database directly, we will ask for a session
# Create a new instance of sessionmaker, then point to our engine (the db)
# in order to use the database :

Session = sessionmaker(db)

# opens an actual session by calling the Session() subclass defined above:

session = Session()

# Given that the 'base' variable is a subclass from the declarative_base, use 
# the .create_all() method from our database metadata.

# creating the database using declarative_base subclass and generate all metadata:
base.metadata.create_all(db)


# ------------ Queries to the database sessions

# Query 1 - select all records from the "Artist" table

# artists = session.query(Artist) # session.query to query the Artist class above
# for artist in artists:  # to iterate over the results found
#     print(artist.ArtistId, artist.Name, sep=" | ") # print each separated columns using dot-notation and "|" on our for-loop


# Query 2 - select only the "Name" column from the "Artist" table

# artists = session.query(Artist) 
# for artist in artists:
#     print(artist.Name)


# Query 3 - select only "Queen" from the "Artist" table

# To find a single artist, the new variable will be 'artist', singular.
# This time, we can use the .filter_by() the Name column to equal Queen
# The .first() method to only give us the first item from the query

# artist = session.query(Artist).filter_by(Name="Queen").first()
# print(artist.ArtistId, artist.Name, sep=" | ")


# Query 4 - select only by "ArtistId" #51 from the "Artist" table

# artist = session.query(Artist).filter_by(ArtistId=51).first()
# print(artist.ArtistId, artist.Name, sep=" | ")

# Query 5 - select only the albums with "ArtistId" #51 on the "Album" table
# albums = session.query(Album).filter_by(ArtistId=51)
# for album in albums:
#     print(album.AlbumId, album.Title, album.ArtistId, sep=" | ")

# Query 6 - select all tracks where the composer is "Queen" from the "Track" table
tracks = session.query(Track).filter_by(Composer="Queen")
for track in tracks:
    print(
        track.TrackId,
        track.Name,
        track.AlbumId,
        track.MediaTypeId,
        track.GenreId,
        track.Composer,
        track.Milliseconds,
        track.Bytes,
        track.UnitPrice,
        sep=" | "
    )
