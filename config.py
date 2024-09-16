import os
# 環境變數模組
from dotenv import load_dotenv

class Config(object):
    # 引用環境變數(env)
    load_dotenv()

    # Database Configuration
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URI") or 'sqlite:///data.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # SECRET_KEY
    SECRET_KEY = os.getenv("SECRET_KEY") or 'A_VERY_LONG_SECRET_KEY'    # 給form使用

    # Flask Gamil Config (SSL | TLS 擇一使用)
    MAIL_SERVER = 'smtp.gmail.com'

    # SSL, Secure Sockets Layer
    # MAIL_PORT = 465
    # MAIL_USE_SSL = True

    # TLS, Transport Layer Security
    MAIL_PORT = 587
    MAIL_USE_TLS = True

    MAIL_USERNAME = os.getenv("MAIL_USERNAME")
    MAIL_PASSWORD = os.getenv("MAIL_PASSWORD")