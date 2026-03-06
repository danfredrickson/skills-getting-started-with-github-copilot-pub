import pytest
from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)

def test_root_redirect():
    # Arrange
    # (No setup needed)


    # Act
    response = client.get("/")

    # Assert
    assert response.status_code in (200, 201)

def test_get_activities():
    # Arrange
    # (No setup needed)

    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200
    assert isinstance(response.json(), dict)

def test_signup_and_unregister():
    # Arrange
    activities = client.get("/activities").json()
    if not activities:
        pytest.skip("No activities defined")
    activity_name = list(activities.keys())[0]
    email = "testuser@example.com"

    # Act
    signup = client.post(f"/activities/{activity_name}/signup?email={email}")

    # Assert
    assert signup.status_code == 200
    assert f"Signed up {email}" in signup.json().get("message", "")

    # Act (unregister)
    unregister = client.post(f"/activities/{activity_name}/unregister?email={email}")

    # Assert
    assert unregister.status_code in (200, 404)
