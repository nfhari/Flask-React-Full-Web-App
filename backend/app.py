from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
# import pymysql

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:''@localhost/flask_react_crud'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = ''
# app.config['MYSQL_DB'] = 'flask_react_crud'

# mysql = pymysql.connect(
#     host = app.config['MYSQL_HOST'],
#     user = app.config['MYSQL_USER'],
#     password= app.config['MYSQL_PASSWORD'],
#     db = app.config['MYSQL_DB']
# )

import routes
#the below code will create all the tables exist in model
with app.app_context():
    db.create_all() 
if __name__ == '__main__':
    app.run(debug=True)