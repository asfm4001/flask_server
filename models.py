# import os

#  取得目前文件資料夾路徑
#  os.path.abspath(os.path.dirname(__file__)) 
#  -> /Users/muchian/Documents/learnPython/learnFlask/ex6
# pjdir = os.path.abspath(os.path.dirname(__file__))

from app import db, login


@login.user_loader
def load_user(user_id):
    return User.query.filter_by(id=user_id).first()

from flask_login import UserMixin
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(20), nullable=False)
    

    def __repr__(self):
        return f'<User {self.username}>'
    