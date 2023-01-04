from typing import List, Dict

from flask_restx import Namespace, Resource
from app.implemented import director_service
from app.dao.model.director import DirectorSchema

directors_ns = Namespace("directors")


@directors_ns.route("/")
class DirectorsViews(Resource):
    """"Представление для множества режиссёров"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.directors_schema = DirectorSchema(many=True)

    def get(self) -> List[Dict]:
        """"Все режиссёры"""
        return self.directors_schema.dump(director_service.get_all())


@directors_ns.route("/<int:uid>")
class DirectorViews(Resource):
    """"Представления для одного режиссёра"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.director_schema = DirectorSchema()

    def get(self, uid: int) -> Dict:
        """Режиссёр по id"""
        return self.director_schema.dump(director_service.get_one(uid))
