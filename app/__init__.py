from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# 引用Config.py 內含db路徑
from config import Config

from flask_bootstrap import Bootstrap
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
bootstrap = Bootstrap(app)
bcrypt = Bcrypt(app)
login = LoginManager(app)
mail = Mail(app)

# login_required 設定
login.login_view = "login"
login.login_message = "You must login to access this page."
login.login_message_category = "info"

# 取代原本路由的位置(app的裝飾器)
from app.routes import *