    # run.py
    from src import create_app  # Importa la "fábrica" desde tu paquete src
    import os

    # Carga la configuración correcta según una variable de entorno
    # Si no se especifica, usa la de desarrollo por defecto
    config_name = os.environ.get('FLASK_CONFIG') or 'development'

    if config_name == 'production':
        from config import ProductionConfig
        app = create_app(ProductionConfig)
    else:
        from config import DevelopmentConfig
        app = create_app(DevelopmentConfig)


    if __name__ == '__main__':
            app.run()