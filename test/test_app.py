import pytest
from config import TestingConfig
from src import create_app


@pytest.fixture
def client():
    """
    Crea un cliente de prueba para la aplicación Flask.
    Esto es una 'fixture' de pytest.
    """
    # Crea una instancia de la app con la configuración de testing
    app = create_app(TestingConfig)

    # El 'test_client' permite simular peticiones a la app sin levantar
    # un servidor
    with app.test_client() as client:
        yield client


def test_hello_route(client):
    """
    GIVEN un cliente de prueba de Flask
    WHEN se hace una petición GET a la ruta '/'
    THEN se debe recibir una respuesta exitosa (código 200)
    y el contenido correcto
    """
    # Hacemos la petición a la ruta raíz
    response = client.get('/')

    # Verificamos que la respuesta sea la correcta
    assert response.status_code == 200
    assert b"DevOps test desde la nueva estructura!" in response.data
