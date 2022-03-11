from numpy import NaN
from starlette.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_ping():
    response = client.get("/ping")
    assert response.status_code == 200
    assert response.json() == {"ping": "pong!"}


def test_ping_value():
    response = client.get("/ping")
    assert response.json()['ping'] == 'pong!'


def test_sequence():
    response = client.get("/sequence")
    assert response.status_code == 200
    assert response.json()['sequence'][1] == 'pong!1'
    assert len(response.json()['sequence']) >= 3


def test_length():
    response = client.get("/sequence")
    assert response.status_code == 200
    assert len(response.json()['sequence']) >= 3


def test_length_not_null():
    response = client.get("/sequence")
    assert response.status_code == 200
    assert len(response.json()['sequence']) != NaN
