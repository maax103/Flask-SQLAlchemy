from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Gituser(db.Model):
    id = db.Column('id', db.Integer, primary_key=True)
    login = db.Column(db.String(150))
    name = db.Column(db.String(150))
    bio = db.Column(db.String(500))

    def __int__(self, id, login, name, bio):
        self.id = id
        self.login = login
        self.name = name
        self.bio = bio

    def to_dict(self, columns=[]):
        if not columns:
            return {"id": self.id, "login": self.login, "name": self.name, "bio": self.bio}
        else:
            return {col: getattr(self, col) for col in columns}