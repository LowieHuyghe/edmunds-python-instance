
from edmunds.auth.models.rolemixin import RoleMixin
from edmunds.database.model import Model


class Role(Model, RoleMixin):
    """
    Role Model
    """

    # __tablename__ = 'role'
    # __bind_key__ = 'users'
