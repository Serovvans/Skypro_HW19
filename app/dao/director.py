from typing import List
from app.dao.model.director import Director


class DirectorDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, uid: int) -> Director:
        return self.session.query(Director).get(uid)

    def get_all(self) -> List[Director]:
        return self.session.query(Director).all()
