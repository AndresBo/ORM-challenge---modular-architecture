from main import db


class Actor(db.Model):
    #define the table name for the db
    __tablename__ = "ACTORS"
    #set the primary key
    id = db.Column(db.Integer,primary_key = True)
    #set rest of attributes
    name = db.Column(db.String())
    gender = db.Column(db.String())
    country = db.Column(db.String())
    dob = db.Column(db.Date())
