from fastapi.testclient import TestClient 
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) #because main is in root whilst this is in subfolder

from main import app
from storage import temp_spot_list


client = TestClient(app)


#When i run the first test it automatically saves for the next tests. I thought it reset between each test but i see now it jsut like running a server.


def test_create_spot():
    response = client.post("/spots", json={
        "name": "Muizenberg",
        "latitude": -34.105,
        "longitude": 18.469,
        "description": "Beginner friendly surf spot"
        })
    assert response.status_code == 200
    assert response.json() == {"spot_id": 1, "name": "Muizenberg", "latitude": -34.105, "longitude": 18.469, "description": "Beginner friendly surf spot"}


def test_read_all_spots():
    response = client.get('/spots')
    assert response.status_code == 200
    assert response.json() == [{"spot_id": 1, "name": "Muizenberg", "latitude": -34.105, "longitude": 18.469, "description": "Beginner friendly surf spot"}]

def test_read_spot():
    response = client.get("/spots/1")
    assert response.status_code == 200
    assert response.json() == {"spot_id": 1, "name": "Muizenberg", "latitude": -34.105, "longitude": 18.469, "description": "Beginner friendly surf spot"}

def test_invalid_spot_id():
    response = client.get("/spots/1000")
    assert response.status_code == 404