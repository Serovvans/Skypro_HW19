from typing import List, Dict

from flask_restx import Namespace, Resource
from flask import request
from app.implemented import movie_service
from app.dao.model.movie import MovieSchema

movies_ns = Namespace("movies")


@movies_ns.route("/")
class MoviesViews(Resource):
    """"Представление для множества фильмов"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.movie_schema = MovieSchema()
        self.movies_schema = MovieSchema(many=True)

    def get(self) -> List[Dict]:
        """"Все фильмы"""
        did = request.args.get("director_id")
        gid = request.args.get("genre_id")

        if did:
            return movie_service.get_all_by_director(did)
        if gid:
            return movie_service.get_all_by_genre(gid)
        return self.movies_schema.dump(movie_service.get_all())

    def post(self) -> Dict:
        """"Добавление фильма"""
        data = request.json

        return self.movie_schema.dump(movie_service.create(data))


@movies_ns.route("/<int:uid>")
class MovieViews(Resource):
    """"Представления для одного фильма"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.movie_schema = MovieSchema()
        self.movies_schema = MovieSchema(many=True)

    def get(self, uid: int) -> Dict:
        """Фильм по id"""
        return self.movie_schema.dump(movie_service.get_one(uid))

    def put(self, uid: int) -> Dict:
        """"Изменение всех данных фильма"""
        data = request.json
        data["id"] = uid

        return self.movie_schema.dump(movie_service.update(data))

    def patch(self, uid: int) -> Dict:
        """"Изменение некоторых данных фильма"""
        data = request.json
        data["id"] = uid

        return self.movie_schema.dump(movie_service.update_partial(data))

    def delete(self, uid: int) -> int:
        """"Удаление фильма"""
        movie_service.delete(uid)
        return 200
