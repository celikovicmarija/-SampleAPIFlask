import sqlite3
# internal representation of an entity-model
# external representation of an entity-resource
# gives flexibilty without polluting the resources
# resource is there to map endpoints
# fin_by_username, or by name do not belong in the resources
# since the client does not interact with those methods, not called by api directly
from db import db


class UserModel(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    #zbog ovog primary_key id je auto increment, pa ga ne ubacujes
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()