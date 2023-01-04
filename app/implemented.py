from app.setup_db import db
from app.dao.movie import MovieDAO
from app.service.movie import MovieService
from app.dao.director import DirectorDAO
from app.service.director import DirectorService
from app.dao.genre import GenreDAO
from app.service.genre import GenreService

movie_dao = MovieDAO(db.session)
movie_service = MovieService(movie_dao)

director_dao = DirectorDAO(db.session)
director_service = DirectorService(director_dao)

genre_dao = GenreDAO(db.session)
genre_service = GenreService(genre_dao)
