import os
# 引入dotenv 將環境變數(env)引用
from dotenv import load_dotenv
load_dotenv()

class Config(object):
    # Database Configuration
    SQLALCHEMY_DATABASE_URI = 'sqlite:///data.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    SECRET_KEY = 'dev'    # 給form使用

    # Flask Gamil Config
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.getenv("GMAIL_USERNAME")
    MAIL_PASSWORD = os.getenv("GMAIL_PASSWORD")