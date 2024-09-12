import os
# 引入dotenv 將環境變數(env)引用
from dotenv import load_dotenv


class Config(object):
    load_dotenv()

    # Database Configuration
    SQLALCHEMY_DATABASE_URI = 'sqlite:///data.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # SECRET_KEY
    SECRET_KEY = os.getenv("SECRET_KEY") or 'A_VERY_LONG_SECRET_KEY'    # 給form使用

    # Flask Gamil Config
    MAIL_SERVER = 'smtp.gmail.com'
    
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    
    # MAIL_PORT = 587
    # MAIL_USE_TLS = True
    MAIL_USERNAME = os.getenv("MAIL_USERNAME")
    MAIL_PASSWORD = os.getenv("MAIL_PASSWORD")