import requests

API_URL = "http://127.0.0.1:8000"


def test_get_index():
    response = requests.get(
        url=f"{API_URL}/"
    )

    assert response.status_code == 200, response.content

    data = response.json()

    assert "Hello" in data
    assert data["Hello"] == "World"


def test_post_mon_post():
    response = requests.post(
        url=f"{API_URL}/mon_post"
    )

    assert response.status_code == 200, response.content

    data = response.json()

    assert "prediction" in data
    assert data["prediction"] in [0, 1, 2, 3]

# FEATURE: GET /health
# reponse: {"status": 1}


def test_get_health():
    response = requests.get(
        url=f"{API_URL}/health"
    )

    assert response.status_code == 200, response.content

    data = response.json()

    assert "status" in data
    assert data["status"] == 1


def test_delete_users():
    # DELETE /users
    # {"action": "user deleted", "user_id": int}

    response = requests.delete(
        url=f"{API_URL}/users"
    )

    assert response.status_code == 200

    data = response.json()

    assert "action" in data
    assert "user_id" in data

    assert data["action"] == "user deleted"
    assert type(data["user_id"]) == int


# GET /bye
# renvoie {"bye": "bye"}

def test_get_bye():
    response = requests.get(
        url=f"{API_URL}/bye"
    )

    assert response.status_code == 200

    data = response.json()

    assert "bye" in data
    assert data["bye"] == "bye"
