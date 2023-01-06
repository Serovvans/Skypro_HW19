from typing import List, Dict
from app.dao.model.movie import Movie


class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, uid: int) -> Movie:
        return self.session.query(Movie).get(uid)

    def get_all(self) -> List[Movie]:
        return self.session.query(Movie).all()

    def get_all_by_director(self, did: int) -> List[Movie]:
        """
        Возвращает все фильмы под режиссёрством указанного id
        :param did: id режиссёра
        :return: Список фильмов данного режиссёра
        """
        return self.session.query(Movie).filter(Movie.director_id == did).all()

    def get_all_by_genre(self, gid: int) -> List[Movie]:
        """
        Возвращает все фильмы указанного жанра
        :param gid: id жанра
        :return: Список фильмов данного жанра
        """
        return self.session.query(Movie).filter(Movie.genre_id == gid).all()

    def get_all_by_year(self, year: int) -> List[Movie]:
        """
        Возвращает все фильмы, выпущенные в указанном году
        :param year: год выпуска фильма
        :return: Список фильмов по году
        """
        return self.session.query(Movie).filter(Movie.year == year).all()

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
