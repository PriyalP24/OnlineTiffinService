class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = "anysecretkey"

    HOST = "localhost"
    DB_NAME = "users"
    DB_USERNAME = "root"
    DB_PASSWORD = "root123"

    IMAGE_UPLOADS = "/static/user.jpeg"

    SESSION_COOKIE_SECURE = True

class ProductionConfig(Config):
    pass

class DevelopmentConfig(Config):
    DEBUG = True

    HOST = "localhost"
    DB_NAME = "cart"
    DB_USERNAME = "root"
    DB_PASSWORD = "root123"

    IMAGE_UPLOADS = "/static/it2.jpeg"

    SESSION_COOKIE_SECURE = False

class TestingConfig(Config):
    TESTING = True

    HOST = "localhost"
    DB_NAME = "cart"
    DB_USERNAME = "root"
    DB_PASSWORD = "root123"

    SESSION_COOKIE_SECURE = False
