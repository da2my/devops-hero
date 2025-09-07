# config.py
import os

class Config:
    """Configuración base, compartida por todos los entornos."""
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'una-clave-secreta-por-defecto'
    DEBUG = False
    TESTING = False

class DevelopmentConfig(Config):
    """Configuración para desarrollo."""
    DEBUG = True
    # Ejemplo: DATABASE_URI = 'sqlite:///dev.db'

class ProductionConfig(Config):
    """Configuración para producción."""
    # Ejemplo: DATABASE_URI = os.environ.get('DATABASE_URI')