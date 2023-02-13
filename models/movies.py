from main import db


class Movie(db.Model):
    #define the table name for the db
    __tablename__ = "MOVIES"
    #set the primary key 
    id = db.Column(db.Integer,primary_key = True)
    #set rest of attributes
    title = db.Column(db.String())
    genre = db.Column(db.String())
    length = db.Column(db.Integer())
    year = db.Column(db.Integer())
