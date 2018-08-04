import os

DEBUG = True
SECRET_KEY = os.urandom(24)
SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:APTX4869@127.0.0.1/test'  # 这是Python3的
SQLALCHEMY_TRACK_MODIFICATIONS = False