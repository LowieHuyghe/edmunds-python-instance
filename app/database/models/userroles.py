
from edmunds.auth.models.userrolesmixin import UserRolesMixin
from edmunds.database.model import Table


UserRolesTable = Table(
    'user_roles',
    *UserRolesMixin,

    #  info={'bind_key': 'users_database'},
)
