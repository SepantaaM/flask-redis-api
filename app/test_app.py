import pytest
from app import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_home_returns_200(client, mocker):
    mocker.patch("app.r.incr", return_value=1)
    response = client.get("/")
    assert response.status_code == 200

def test_set_message_missing_field(client):
    response = client.post("/message", json={})
    assert response.status_code == 400

def test_set_message_success(client, mocker):
    mocker.patch("app.r.set", return_value=True)
    response = client.post("/message", json={"message": "hello"})
    assert response.status_code == 200

def test_get_message(client, mocker):
    mocker.patch("app.r.get", return_value="hello")
    response = client.get("/message")
    assert response.status_code == 200
