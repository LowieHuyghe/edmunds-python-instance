
from edmunds.database.table import Table, Column, Integer, String


UsersTable = Table('users',
                   Column('id', Integer, primary_key=True),
                   Column('name', String(50)),

                   # info={'bind_key': 'users_database'},
                   )
