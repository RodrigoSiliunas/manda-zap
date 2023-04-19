import datetime
from os import environ

"""
==========================================================================
 ➠ Section By: Rodrigo Siliunas (https://github.com/RodrigoSiliunas)
 ➠ Related system: App Configuration
==========================================================================
"""

class Config:
    JSON_SORT_KEYS = False
    THREADED = False
    JWT_ACCESS_TOKEN_EXPIRES = datetime.timedelta(minutes=20)


class ProductionConfig(Config):
    FLASK_ENV = 'production'
    JWT_SECRET_KEY = environ.get('SECRET_KEY')
    MONGODB_SETTINGS = {
        'DB': environ.get('MONGO_DB_NAME'),
        'HOST': environ.get('MONGO_URI')
    }
    DEBUG = False
    TESTING = False
    THREADED = True


class DevelopmentConfig(Config):
    FLASK_ENV = 'development'
    JWT_SECRET_KEY = 'THIS IS A SECRET'
    MONGODB_SETTINGS = {
        'DB': 'mandazap',
        'HOST': 'mongodb+srv://rodrigosiliunas12:C4Jj5VtHdZQZcNa@clusterac.6ssaov6.mongodb.net/mandazap'
    }
    DEBUG = True
    TESTING = True
    THREADED = False