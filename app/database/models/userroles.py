
from edmunds.database.model import db


UserRolesTable = db.Table(
    'user_roles',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('role_id', db.Integer, db.ForeignKey('role.id')),

    #  info={'bind_key': 'users_database'},
)
