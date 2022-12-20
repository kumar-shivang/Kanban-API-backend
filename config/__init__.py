# This file contains configuration variables for the application.
from datetime import timedelta
from os import path
basedir = path.abspath(path.dirname(__file__))
class Config(object):
    SQLALCHEMY_DB_DIR = None
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(days=1)
    JWT_REFRESH_TOKEN_EXPIRES = 30
    JWT_BLACKLIST_ENABLED = True
    JWT_BLACKLIST_TOKEN_CHECKS = ['access', 'refresh']
    JWT_TOKEN_LOCATION = ['cookies','json']
    JWT_COOKIE_CSRF_PROTECT = False
    JWT_COOKIE_SECURE = False


class DevelopmentConfig(Config):
    SQLALCHEMY_DB_DIR = path.join(basedir, '../')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + path.join(SQLALCHEMY_DB_DIR, 'database.sqlite3')
    DEBUG = True
    TEST = True
    SECRET_KEY = 'test_secret_key'
    JWT_SECRET = 'test_jwt-secret'
