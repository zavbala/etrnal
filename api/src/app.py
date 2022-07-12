from flask import Flask

from src import items
from src.extensions import cache, cors
from src.settings import DevConfig


def create_app(config_object=DevConfig):
    """Root"""

    name, _ = __name__.split(".")
    app = Flask(name)

    app.config.from_object(config_object)

    register_extensions(app)
    register_blueprints(app)

    return app


def register_extensions(app: Flask):
    """Main Extensions"""

    cors.init_app(app)
    cache.init_app(app)


def register_blueprints(app: Flask):
    """Main Blueprints"""

    origins = app.config.get("CORS_ORIGIN_WHITELIST", "*")
    cors.init_app(items.views.blueprint, origins=origins)
    app.register_blueprint(items.views.blueprint)
