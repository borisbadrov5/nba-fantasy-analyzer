import os


class Config(object):
    DATABASE_URL = os.environ.get('DATABASE_URL').replace("://", "ql://", 1)
    SQLALCHEMY_DATABASE_URI = DATABASE_URL
    SQLALCHEMY_TRACK_MODIFICATIONS = False