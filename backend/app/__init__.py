from flask import Flask
from flask_cors import CORS
from backend.config import config

def create_app(config_name='default'):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    CORS(app)

    from backend.app.api import bp as api_bp
    app.register_blueprint(api_bp)

    return app