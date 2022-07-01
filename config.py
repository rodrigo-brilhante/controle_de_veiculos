SECRET_KEY = '@nork'

SQLALCHEMY_DATABASE_URI = \
    '{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format(
        SGBD = 'mysql+mysqlconnector',
        usuario = 'root',
        senha = 'nork',
        servidor = 'localhost',
        database = 'nork_town'
    )