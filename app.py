from flask import Flask
from model.serializer import configure
from router.config_router import bp_config
from router.revenda_router import bp_revenda


def create_app():
    app = Flask(__name__)

    configure(app)

    app.register_blueprint(bp_revenda)
    app.register_blueprint(bp_config)

    return app
