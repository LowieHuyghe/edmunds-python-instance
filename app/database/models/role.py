
from edmunds.auth.models.rolemixin import RoleMixin
from edmunds.database.model import db


class Role(db.Model, RoleMixin):
    """
    Role Model
    """

    # __tablename__ = 'role'
    # __bind_key__ = 'users'
