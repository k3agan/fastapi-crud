import json
import pytest
from app.api import crud


def test_create_note(test_app, monkeypatch):
    payload = {
        "title": "Test note",
        "description": "This is a test note."
    }
    monkeypatch.setattr(crud, "post", lambda payload: 1)

    response = test_app.post("/notes", data=json.dumps(payload))
    assert response.status_code == 201
    assert response.json() == {
        "id": 1,
        "title": "Test note",
        "description": "This is a test note."
    }
