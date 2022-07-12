import os
import pathlib
from datetime import timedelta


class Config(object):
    """Base configuration"""

    SECRET_KEY = os.environ.get("ETERNAL_SECRET", "secret-key")
    APP_DIR = pathlib.Path(__file__).parent
    PROJECT_ROOT = os.path.abspath(os.path.join(APP_DIR, os.pardir))
    CACHE_TYPE = "SimpleCache"
    JWT_AUTH_USERNAME_KEY = "email"
    JWT_AUTH_HEADER_PREFIX = "Token"
    CORS_ORIGIN_WHITELIST = [
        "http://0.0.0.0:3000",
        "http://localhost:3000",
        "http://127.0.0.1:3000",
    ]
    JWT_HEADER_TYPE = "Token"


class ProdConfig(Config):
    """Production configuration"""

    ENV = "prod"
    DEBUG = False


class DevConfig(Config):
    """Development configuration"""

    ENV = "dev"
    DEBUG = True
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(10**6)


class TestConfig(Config):
    """Test configuration"""

    TESTING = True
    DEBUG = True
