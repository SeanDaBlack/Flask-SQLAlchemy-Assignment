from src.models import Movie, db


class MovieRepository:

    def get_all_movies(self):
        # TODO get all movies from the DB
        print('getting all')
        return Movie.query.all()

    def get_movie_by_id(self, movie_id):
        # TODO get a single movie from the DB using the ID

        return Movie.query.get(movie_id)

    def create_movie(self, title, director, rating):
        # TODO create a new movie in the DB

        movie = Movie(movie_id=len(Movie.query.all())+1,
                      title=title, director=director, rating=rating)
        db.session.add(movie)
        db.session.commit()
        return movie

    def search_movies(self, title):
        # TODO get all movies matching case insensitive substring (SQL LIKE, use google for how to do with SQLAlchemy)
        return Movie.query.filter(Movie.title.like(f'%{title}%')).all()


# Singleton to be used in other modules
movie_repository_singleton = MovieRepository()
