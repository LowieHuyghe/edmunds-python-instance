
from flask_security import SQLAlchemyUserDatastore
from app.database.models.user import User
from app.database.models.role import Role


SECURITY_PASSWORD_HASH = 'sha512_crypt'
SECURITY_PASSWORD_SALT = 'my very long salt'
APP = {

    # ------------------------------------------------------------
    # Authentication
    # ------------------------------------------------------------
    #
    # Authentication is configured here.
    #
    # Authentication Drivers:
    # from flask_security import SQLAlchemyUserDatastore
    #

    'auth':
    {
        'enabled': False,
        'instances':
        [
            {
                'name': 'authsqlalchemy',
                'driver': SQLAlchemyUserDatastore,
                'models': {
                    'user': User,
                    'role': Role,
                },
            },
        ],
    },

}
