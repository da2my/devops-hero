from flask import Flask
from config import Config


def create_app(config_class=Config):
    """
    Función fábrica para crear la instancia de la aplicación Flask.
    """
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Registrar el Blueprint desde el módulo 'main' necesaria en Flask
    # para evitar importaciones circulares.
    from .main.routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # Aquí podrías registrar más Blueprints o extensiones

    return app
