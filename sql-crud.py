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

alan_turing = Programmer(
    first_name="Alan",
    last_name="Turing",
    gender="M",
    nationality="British",
    famous_for="Modern Computing"
)

grace_hopper = Programmer(
    first_name="Grace",
    last_name="Hopper",
    gender="F",
    nationality="American",
    famous_for="COBOL Language"
)

margaret_hamilton = Programmer(
    first_name="Margaret",
    last_name="Hamilton",
    gender="F",
    nationality="American",
    famous_for="Apollo 11"
)

bill_gates = Programmer(
    first_name="Bill",
    last_name="Gates",
    gender="M",
    nationality="American",
    famous_for="Microsoft"
)

tim_berners_lee = Programmer(
    first_name="Tim",
    last_name="Berners-Lee",
    gender="M",
    nationality="British",
    famous_for="World Wide Web"
)

stuart_roeszler = Programmer(
    first_name="Stuart",
    last_name="Roeszler",
    gender="M",
    nationality="Australian",
    famous_for="Providence Systems"
)

tim_nelson = Programmer(
    first_name="Tim",
    last_name="Nelson",
    gender="M",
    nationality="Irish-American",
    famous_for="Code Institute"
)

# ------------ Add each instance of out record 'Programmers' to the session
# session.add(ada_lovelace)
# session.add(alan_turing)
# session.add(grace_hopper)
# session.add(margaret_hamilton)
# session.add(bill_gates)
# session.add(tim_berners_lee)
# session.add(stuart_roeszler)
# session.add(tim_nelson)


# ------------ Update single record
# programmer = session.query(Programmer).filter_by(id=7).first()
# programmer.famous_for = "Providence Systems"
# session.commit()


# ------------ Update multiple records (to be the standard query)
# people = session.query(Programmer)
# for person in people:
#     if person.gender == "F":
#         person.gender = "Female"
#     elif person.gender == "M":
#         person.gender = "Male"
#     else:
#         print("Gender not defined")
#     session.commit()


# ------------ Deleting a single record
fname = input("Enter a first name: ")
lname = input("Enter a last name: ")
programmer = session.query(Programmer).filter_by(first_name=fname, last_name=lname).first() # query the Progrmmer table
# ------ defensive programming to check to double-check that it's the correct programmer being found:
if programmer is not None:
    print("Programmer Found: ", programmer.first_name + " " + programmer.last_name)
    conformation = input("Are you sure you want to delete this record? (y/n) ")
    if conformation.lower() == "y":
        session.delete(programmer)
        session.commit()
        print("Programmer has been deleted")
    else:
        print("Programmer not deleted")
else:
    print("No records found")


# ------------ Deleting a multiple records
# programmers = session.query(Programmer)
# for programmer in programmers:
#     session.delete(programmer)


# ------ defensive programming to check to double-check that it's the correct programmer being found:
# programmers = session.query(Programmer)
# if programmers is not None:
#     print("Programmers Found: ", programmers)
#     conformation = input("Are you sure you want to delete all records in database? (y/n) ")
#     if conformation.lower() == "y":
#         session.delete(programmers)
#         session.commit()
#         print("Programmers content has been deleted")
#     else:
#         print("Programmers content not deleted")
# else:
#     print("No records found in database")

# ------------ Commit session to the database
# session.commit()


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
