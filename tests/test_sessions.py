from fastapi.testclient import TestClient 
import pytest
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) #because main is in root whilst this is in subfolder
from main import app
from storage_temp import temp_session_list, temp_spot_list


client = TestClient(app)

@pytest.fixture(autouse=True)
def spot():
    # clear both lists so each test starts clean
    temp_session_list.clear()
    temp_spot_list.clear()

    # create a spot to use in tests
    response = client.post("/spots", json={
        "name": "Muizenberg",
        "latitude": -34.105,
        "longitude": 18.469,
        "description": "Beginner friendly surf spot"
    })
    return response.json()  # returns the created spot (with spot_id)

#helper function
def create_session(spot):
    response = client.post("/sessions", json={
        "spot_id": spot["spot_id"],
        "date": "2025-09-18",
        "time": "07:30:00",
        "rating": 4,
        "wave_height": 1.8,
        "tide": "mid",
        "waves_caught": 6,
        "notes": "Great morning surf, small but clean waves."
        })
    return response
    

#tests

def test_create_session(spot):
    response = create_session(spot)
    assert response.status_code == 201
    assert response.json()["spot_id"] == spot["spot_id"]

def test_read_all_sessions(spot):
    create_session(spot)
    response = client.get("/sessions")
    assert response.status_code == 200
    data = response.json()
    assert type(data) == list
    assert len(data) == 1
    assert data[0]["spot_id"] == spot["spot_id"]

def test_read_session(spot):
    create_session(spot)
    response = client.get("/sessions/1")
    assert response.status_code == 200
    data = response.json()
    assert data["session_id"] == 1
    assert data["waves_caught"] == 6

def test_invalid_session_id(spot):
    create_session(spot)
    response = client.get("/sessions/1000")
    assert response.status_code == 404
    data = response.json()
    assert data["detail"] == "Session with the given ID does not exist."

def test_invalid_create_session(spot):
    response = client.post("/sessions", json={
        "spot_id": spot["spot_id"],
        "date": "12 June 2025",
        "time": "07:30:00",
        "rating": 4,
        "wave_height": 1.8,
        "tide": "mid",
        "waves_caught": 6,
        "notes": "Great morning surf, small but clean waves."
        })
    assert response.status_code == 422

def test_create_session_with_invalid_spot():
    response = client.post("/sessions", json={
        "spot_id": 999,  # no such spot
        "date": "2025-09-18",
        "time": "07:30:00",
        "rating": 3,
        "wave_height": 1.0,
        "tide": "low",
        "waves_caught": 4
    })
    assert response.status_code == 404
    assert response.json()["detail"] == "Spot not found"

    


