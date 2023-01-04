from flask_restx import Namespace, Resource
from app.implemented import director_service

directors_ns = Namespace("directors")


@directors_ns.route("/")
class DirectorsViews(Resource):
    """"Представление для множества режиссёров"""
    def get(self):
        """"Все режиссёры"""
        return director_service.get_all()


@directors_ns.route("/<int:uid>")
class DirectorViews(Resource):
    """"Представления для одного режиссёра"""
    def get(self, uid: int):
        """Режиссёр по id"""
        return director_service.get_one(uid)
