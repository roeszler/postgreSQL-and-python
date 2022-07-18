"""
The reason that we no longer need to import the Table class, is because with the ORM,
we're not going to create tables, but instead, we'll be creating Python classes.
"""
from sqlalchemy import (
    create_engine, Column, Integer, String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# ------------ Executing the instructions from the "chinook" database
db = create_engine("postgresql:///chinook")
base = declarative_base()


# ------------ The CREATE part of C.R.U.D:

# ------------ New create a class-based model for the "Programmer" table
class Programmer(base):
    __tablename__ = "Programmer"
    id = Column(Integer, primary_key=True) # as this is a PK, it will auto increment
    first_name = Column(String)
    last_name = Column(String)
    gender = Column(String)
    nationality = Column(String)
    famous_for = Column(String)


# ------------ Create the session for the database to be accessed
Session = sessionmaker(db)
session = Session()
base.metadata.create_all(db)


# ------------ Create records on our 'Programmer' table
ada_lovelace = Programmer(
    first_name="Ada",
    last_name="Lovelace",
    gender="F",
    nationality="British",
    famous_for="First Programmer"
)

# ------------ Add each instance of out record 'Programmers' to the session
# session.add(ada_lovelace)

# ------------ Commit session to the database
session.commit()


# ------------ The READ part of C.R.U.D:

# ------------ Query the database to find all Programmers
programmers = session.query(Programmer)
for programmer in programmers:
    print(
        programmer.id,
        programmer.first_name + " " + programmer.last_name,
        programmer.gender,
        programmer.nationality,
        programmer.famous_for,
        sep=" | "
    )
