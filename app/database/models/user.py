
from edmunds.database.model import relationship, backref
from edmunds.auth.models.user import User as EdmundsUser
from app.database.models.role import Role
from app.database.models.userroles import UserRolesTable


class User(EdmundsUser):
    """
    User Model
    """

    roles = relationship(Role, backref=backref(EdmundsUser.__tablename__, lazy='dynamic'), secondary=UserRolesTable)
