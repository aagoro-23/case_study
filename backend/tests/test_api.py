from fastapi.testclient import TestClient
from app.main import app
from tests.constants import OUTPUTS

client = TestClient(app=app)


def test_api_server_with_query(request_inputs):
    response = client.get(f"/calculation{request_inputs}")
    assert response.status_code == 200
    assert response.json() == OUTPUTS


def test_index():
    response = client.get("/")
    assert response.status_code == 200
    assert (
        response.json()
        == "Welcome to my application. To calculate the discrete-time dynamical system, GET /calculation."
    )
