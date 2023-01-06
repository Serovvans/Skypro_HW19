from typing import List, Dict
from app.dao.model.movie import Movie
from app.dao.movie import MovieDAO


class MovieService:
    def __init__(self, dao: MovieDAO):
        self.dao = dao

    def get_one(self, uid: int) -> Movie:
        return self.dao.get_one(uid)

    def get_all(self) -> List[Movie]:
        return self.dao.get_all()

    def get_all_by_genre(self, gid: int) -> List[Movie]:
        """
        Возвращает все фильмы указанного жанра
        :param gid: id жанра
        :return: Список фильмов данного жанра
        """
        return self.dao.get_all_by_genre(gid)

    def get_all_by_director(self, did: int) -> List[Movie]:
        """
        Возвращает все фильмы под режиссёрством указанного id
        :param did: id режиссёра
        :return: Список фильмов данного режиссёра
        """
        return self.dao.get_all_by_director(did)

    def get_all_by_year(self, year: int) -> List[Movie]:
        """
        Возвращает все фильмы, выпущенные в указанном году
        :param year: год выпуска фильма
        :return: Список фильмов по году
        """
        return self.dao.get_all_by_year(year)

    def create(self, data: Dict) -> Movie:
        """
        Создаёт новый фильм и добавляет его в базу
        :param data: информация о фильме
        :return: объект созданного фильма
        """
        return self.dao.create(data)

    def update(self, data: Dict) -> Movie:
        """
        Обновляет ПОЛНОСТЬЮ информацию об указанном фильме
        :param data:
        :return:
        """
        uid = data.get('id')

        movie = self.get_one(uid)

        movie.title = data['title']
        movie.description = data['description']
        movie.trailer = data['trailer']
        movie.year = data['year']
        movie.rating = data['rating']
        movie.genre_id = data['genre_id']
        movie.director_id = data['director_id']

        return self.dao.update(movie)

    def update_partial(self, data: Dict) -> Movie:
        """
        Обновляет ЧАСТИЧНО информацию об указанном фильме
        :param data:
        :return:
        """
        uid = data.get('id')

        movie = self.get_one(uid)

        if "title" in data:
            movie.title = data['title']
        if "description" in data:
            movie.description = data['description']
        if "trailer" in data:
            movie.trailer = data['trailer']
        if "year" in data:
            movie.year = data['year']
        if "rating" in data:
            movie.rating = data['rating']
        if "genre_id" in data:
            movie.genre_id = data['genre_id']
        if "director_id" in data:
            movie.director_id = data['director_id']

        return self.dao.update(movie)

    def delete(self, uid: int) -> None:
        """
        Удаляет фильм из базы данных
        :param uid: id фильма
        """
        return self.dao.delete(uid)
