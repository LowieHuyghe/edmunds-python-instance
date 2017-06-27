
from edmunds.database.model import Model, mapper
from app.database.tables.userstable import UsersTable


class User(Model):
    """
    User Model
    """

    __table__ = UsersTable

    def __init__(self, name):
        """
        Constructor
        :param name:    The name of the user
        """
        self.name = name

    def __repr__(self):
        return '<User name="%s" id="%s"/>' % (self.name, self.id)


mapper(User, UsersTable)
