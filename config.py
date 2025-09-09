import os
from dotenv import load_dotenv

# Carga las variables del archivo .env en el entorno
basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


class Config:
    """Configuración base, compartida por todos los entornos."""
    SECRET_KEY = os.environ.get('SECRET_KEY')


class DevelopmentConfig(Config):
    """Configuración para desarrollo."""
    print("Cargando configuración de desarrollo")
    DEBUG = True
    # Ejemplo: DATABASE_URI = 'sqlite:///dev.db'


class ProductionConfig(Config):
    """Configuración para producción."""
    # Ejemplo: DATABASE_URI = os.environ.get('DATABASE_URI')
    pass

# class TestingConfig(Config):  
#     """Configuración para testing."""
#     pass

# Diccionario para mapear nombres a clases
# config_by_name = {
    # 'development': DevelopmentConfig,
    # 'testing': TestingConfig,
    # 'production': ProductionConfig,
    # 'default': DevelopmentConfig
# }
 