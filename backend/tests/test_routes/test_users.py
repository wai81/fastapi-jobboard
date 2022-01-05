import json


def test_create_user(client):
    data = {"username":"test",
            "email":"test@test.com",
            "password":"123456"}
    response = client.post("/users/",json.dumps(data))
    assert response.status_code == 200
    assert response.json()["email"] == "test@test.com"
    assert response.json()["is_active"] == True