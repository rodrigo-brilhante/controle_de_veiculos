import os
SECRET_KEY = '@nork'
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = \
    'mysql+mysqlconnector://{}:{}@{}/{}'.format(
        os.getenv('DB_USER', 'root'),
        os.getenv('DB_PASSWORD', 'nork'),
        os.getenv('DB_HOST', 'mysql'),
        os.getenv('DB_NAME', 'nork_town')
    )
    