from typing import List, Dict
from app.dao.model.movie import Movie, MovieSchema


class MovieDAO:
    def __init__(self, session):
        self.session = session
        self.movie_schema = MovieSchema()
        self.movies_schema = MovieSchema(many=True)

    def get_one(self, uid: int) -> Dict:
        return self.movie_schema.dump(self.session.query(Movie).get(uid))

    def get_all(self) -> List[Dict]:
        return self.movies_schema.dump(self.session.query(Movie).all())

    def get_all_by_director(self, did: int) -> List[Dict]:
        """
        Возвращает все фильмы под режиссёрством указанного id
        :param did: id режиссёра
        :return: Список фильмов данного режиссёра
        """
        return self.movies_schema.dump(self.session.query(Movie).filter(Movie.director_id == did).all())

    def get_all_by_genre(self, gid: int) -> List[Dict]:
        """
        Возвращает все фильмы указанного жанра
        :param gid: id жанра
        :return: Список фильмов данного жанра
        """
        return self.movies_schema.dump(self.session.query(Movie).filter(Movie.genre_id == gid).all())

    def create(self, data: Dict) -> Movie:
        """
        Создаёт новый фильм и добавляет его в базу
        :param data: информация о фильме
        :return: объект созданного фильма
        """
        movie = Movie(**data)

        self.session.add(movie)
        self.session.commit()

        return movie

    def update(self, movie: Movie) -> Movie:
        """
        Обновляет информацию об указанном фильме
        :param movie:
        :return:
        """

        self.session.add(movie)
        self.session.commit()

        return movie

    def delete(self, uid: int) -> None:
        """
        Удаляет фильм из базы данных
        :param uid: id фильма
        """
        movie = self.get_one(uid)

        self.session.delete(movie)
        self.session.commit()
