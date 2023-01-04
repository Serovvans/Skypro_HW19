from flask_restx import Namespace, Resource
from flask import request
from app.implemented import movie_service

movies_ns = Namespace("movies")


@movies_ns.route("/")
class MoviesViews(Resource):
    """"Представление для множества фильмов"""
    def get(self):
        """"Все фильмы"""
        did = request.args.get("director_id")
        gid = request.args.get("genre_id")

        if did:
            return movie_service.get_all_by_director(did)
        if gid:
            return movie_service.get_all_by_genre(gid)
        return movie_service.get_all()

    def post(self):
        """"Добавление фильма"""
        data = request.json

        return movie_service.create(data)


@movies_ns.route("/<int:uid>")
class MovieViews(Resource):
    """"Представления для одного фильма"""
    def get(self, uid: int):
        """Фильм по id"""
        return movie_service.get_one(uid)

    def put(self, uid: int):
        """"Изменение всех данных фильма"""
        data = request.json
        data["id"] = uid

        return movie_service.update(data)

    def patch(self, uid: int):
        """"Изменение некоторых данных фильма"""
        data = request.json
        data["id"] = uid

        return movie_service.update_partial(data)

    def delete(self, uid: int):
        """"Удаление фильма"""
        movie_service.delete(uid)
