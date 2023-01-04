from flask_restx import Namespace, Resource
from app.implemented import genre_service

genres_ns = Namespace("genres")


@genres_ns.route("/")
class GenresViews(Resource):
    """"Представление для множества жанров"""
    def get(self):
        """"Все жанры"""
        return genre_service.get_all()


@genres_ns.route("/<int:uid>")
class GenreViews(Resource):
    """"Представления для одного жанра"""
    def get(self, uid: int):
        """Жанр по id"""
        return genre_service.get_one(uid)
