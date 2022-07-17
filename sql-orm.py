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
    __tabename__ = "Artist"  # creates the table
    ArtistId = Column(Integer, primary_key=True) # identifies Primary Key
    Name = Column(String) # indicates sub-columns

# create a class-based model for the "Album" table
class Album(base):
    __tabename__ = "Album"
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