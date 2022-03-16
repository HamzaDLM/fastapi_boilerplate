from fastapi.testclient import TestClient
from main import app
import json


client = TestClient(app)

payload = json.dumps({})
headers= {'Content-Type': 'application/json'}


def test_example():
    response = client.post("/endpoint1",
                           data=payload,
                           headers=headers)
    assert response.status_code == 201