from starlette.testclient import TestClient

from app.main import app

# client = TestClient(app)


def test_ping(test_app):
    response = test_app.get("/ping")
    assert response.status_code == 200
    assert response.json() == {"ping": "pong!"}


def test_ping_value(test_app):
    response = test_app.get("/ping")
    assert response.json()['ping'] == 'pong!'


def test_sequence(test_app):
    response = test_app.get("/sequence")
    assert response.status_code == 200
    assert response.json()['sequence'][1] == 'pong!1'
    assert len(response.json()['sequence']) >= 3


def test_length(test_app):
    response = test_app.get("/sequence")
    assert response.status_code == 200
    assert len(response.json()['sequence']) >= 3


def test_length_not_null(test_app):
    response = test_app.get("/sequence")
    assert response.status_code == 200
