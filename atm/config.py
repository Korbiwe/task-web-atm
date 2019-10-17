import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    DEBUG = os.environ.get('FLASK_DEBUG', True)
    SQLALCHEMY_DATABASE_URI = 'postgresql://docker@db/web_atm'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
