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
import jwt  # 使用decode, encode
from flask import current_app   # 使用config設定
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(20), nullable=False)
    avatar_img = db.Column(db.String(120), default="/static/asset/default_avatar.png", nullable=False)

    # 設定 與Post關聯
    # relationship(tableName, 反向關聯)
        # bacjref(反向關聯變數名稱, 單向關聯) e.g. user無post則不創建post table
    posts = db.relationship("Post", backref=db.backref("author", lazy=True))
    

    def __repr__(self):
        return f'<User {self.username}>'
    def generate_reset_password_token(self):
        # secret_key 使用config設定的SERCET_KEY
        return  jwt.encode({"id": self.id}, current_app.config["SECRET_KEY"], algorithm="HS256")
    
    # 原方法為class, 需傳入object將其實體化
    # @staticmethod可使方法直接實體化(無需傳入self) -> 美觀
    @staticmethod
    def check_reset_password_token(token):
        # 若token對映user存在, 返回user
        # 否則回傳null
        try:
            data = jwt.decode(token, current_app.config["SECRET_KEY"], algorithms="HS256")
            return User.query.filter_by(id=data["id"]).first()
        except:
            return

from datetime import datetime
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140), nullable=False)
    timestramp = db.Column(db.DateTime, default=datetime.utcnow())
    # 設定foreign key, 與User中的id關聯(table name預設為class name)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)

    def __repr__(self):
        return '<Post {}>'.format(self.body)