from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask('__name__')
app.config.from_pyfile('config.py')
   
db = SQLAlchemy(app)

from views_usuarios import *
from views_carros import *

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=False)