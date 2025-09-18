from fastapi.testclient import TestClient 
import pytest
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) #because main is in root whilst this is in subfolder

from main import app
from storage import temp_spot_list #only need if reseting list


client = TestClient(app)

#        When i run the first test it automatically saves for the next tests. I thought it reset between each test but i see now it jsut like running a server.
@pytest.fixture(autouse=True)     # resets list between tests.
def clear_storage():
    temp_spot_list.clear()

#helper function
def create_spot():
    response = client.post("/spots", json={
        "name": "Muizenberg",
        "latitude": -34.105,
        "longitude": 18.469,
        "description": "Beginner friendly surf spot"
        })
    return response


#tests

def test_create_spot():
    response = create_spot()
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Muizenberg" #Hardcoding expected JSON (entire thing) can lead to errors later if i change/add fields.
    assert data["spot_id"] == 1

def test_read_all_spots():
    create_spot()
    response = client.get('/spots')
    assert response.status_code == 200
    assert type(response.json()) == list

def test_read_spot():
    create_spot()
    response = client.get("/spots/1")
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Muizenberg" 
    assert data["spot_id"] == 1

def test_invalid_spot_id():
    create_spot()
    response = client.get("/spots/1000")
    assert response.status_code == 404
    data = response.json()
    assert data["detail"] == "Spot with the given ID does not exist."


def test_invalid_create_spot():
    response = client.post("/spots", json={
        "name": 5,
        "latitude": -34.105,
        "longitude": 18.469,
        "description": "Beginner friendly surf spot"
        })
    assert response.status_code == 422


def test_sessions_at_spot():
    create_spot()
    session = client.post("/sessions", json={
  "spot_id": 1,
  "date": "2025-09-18",
  "time": "07:30:00",
  "rating": 4,
  "wave_height": 1.8,
  "tide": "mid",
  "waves_caught": 6,
  "notes": "Great morning surf, small but clean waves."
})
    response = client.get("/spots/1/sessions")
    assert response.status_code == 200
    data = response.json()
    assert type(data) == list
    assert data[0]["session_id"] == 1