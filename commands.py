from main import db
from flask import Blueprint
from main import bcrypt
from models.actor import Actor
from models.movie import Movie
from models.user import User


# previously we were passing app variable with @app.cli.command(). But this is considered bad
# practive (WHY?) so we use a Blueprint like controllers
db_commands = Blueprint("db",__name__)

@db_commands.cli.command("create")
def create_db():
    db.create_all()
    print("Tables created")


@db_commands.cli.command("seed")
def seed_db():
    movie1 = Movie(
      title = "Jurassic Park",
      genre = "Action",
      length = "120",
      year = 1994
    )
    db.session.add(movie1)

    movie2 = Movie(
      title = "Dune",
      genre = "Science Fiction",
      length = 180,
      year = 2020
    )
    db.session.add(movie2)

    actor1 = Actor(
      name = "Robin Williams",
      gender = "Male",
      country = "USA",
      dob = '1950-10-01',
    )
    db.session.add(actor1)

    actor2 = Actor(
      name = "Ethan Hawke",
      gender = "Male",
      country = "USA",
      dob = '1950-10-01',
    )
    db.session.add(actor2)

    actor3 = Actor(
      name = "Uma Thurman",
      gender = "Female",
      country = "USA",
      dob = '1950-10-01',
    )
    db.session.add(actor3)


    admin_user = User(
      email = "admin",
      password = bcrypt.generate_password_hash("password123").decode("utf-8"),
      admin = True
    )
    db.session.add(admin_user)

    db.session.commit()
    print("Tables seeded")


@db_commands.cli.command("drop")
def drop_db():
    db.drop_all()
    print("Tables dropped")
