from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# 引入flask-bootstrap
from flask_bootstrap import Bootstrap
Bootstrap(app)

# 引入flask-bcrypt
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

app.config['SECRET_KEY'] = 'dev'    # 給form使用
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# 引入flask-login
from flask_login import LoginManager
login = LoginManager(app)

# login_required 設定
login.login_view = "login"
login.login_message = "You must login to access this page."
login.login_message_category = "info"

# 取代原本路由的位置(app的裝飾器)
from routes import *


