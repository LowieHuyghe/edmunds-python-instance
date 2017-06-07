
from edmunds.database.model import db, Model


class User(Model):
    """
    User Model
    """

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
