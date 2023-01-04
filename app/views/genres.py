from typing import List, Dict

from flask_restx import Namespace, Resource
from app.implemented import genre_service
from app.dao.model.genre import GenreSchema

genres_ns = Namespace("genres")


@genres_ns.route("/")
class GenresViews(Resource):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.genres_schema = GenreSchema(many=True)

    """"Представление для множества жанров"""
    def get(self) -> List[Dict]:
        """"Все жанры"""
        return self.genres_schema.dump(genre_service.get_all())


@genres_ns.route("/<int:uid>")
class GenreViews(Resource):
    """"Представления для одного жанра"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.genre_schema = GenreSchema()

    def get(self, uid: int) -> Dict:
        """Жанр по id"""
        return self.genre_schema.dump(genre_service.get_one(uid))
