from typing import List, Dict
from app.dao.model.genre import Genre, GenreSchema


class GenreDAO:
    def __init__(self, session):
        self.session = session
        self.genre_schema = GenreSchema()
        self.genres_schema = GenreSchema(many=True)

    def get_one(self, uid: int) -> Dict:
        return self.genre_schema.dump(self.session.query(Genre).get(uid))

    def get_all(self) -> List[Dict]:
        return self.genres_schema.dump(self.session.query(Genre).all())
