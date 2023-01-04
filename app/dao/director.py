from typing import List, Dict
from app.dao.model.director import Director, DirectorSchema


class DirectorDAO:
    def __init__(self, session):
        self.session = session
        self.director_schema = DirectorSchema()
        self.directors_schema = DirectorSchema(many=True)

    def get_one(self, uid: int) -> Dict:
        return self.director_schema.dump(self.session.query(Director).get(uid))

    def get_all(self) -> List[Dict]:
        return self.directors_schema.dump(self.session.query(Director).all())
