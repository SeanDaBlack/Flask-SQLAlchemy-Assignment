from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


# TODO - Create SQLAlchemy DB and Movie model
class Movie(db.Model):
    movie_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    director = db.Column(db.String(255), nullable=False)
    rating = db.Column(db.Integer)
