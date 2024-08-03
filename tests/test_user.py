def test_update_user_profile(client, test_user, session):
    response = client.put(
        "/api/user/profile/update",
        json={"name": "New Name", "bio": "New Bio", "location": "New Location"},
        headers={"Authorization": f"Bearer {test_user['token']}"},
    )
    assert response.status_code == 200
    assert response.json()["name"] == "New Name"

def test_upgrade_professional_status(client, admin_user, session):
    response = client.post(
        "/api/admin/user/professional-status",
        json={"user_id": 2},
        headers={"Authorization": f"Bearer {admin_user['token']}"},
    )
    assert response.status_code == 200
    assert response.json()["professional_status"] is True

def test_search_users_by_username(client, session):
    response = client.get("/users?username=testuser")
    assert response.status_code == 200
    assert any(user['username'] == 'testuser' for user in response.json())

def test_filter_users_by_role(client, session):
    response = client.get("/users?role=ADMIN")
    assert response.status_code == 200
    assert all(user['role'] == 'ADMIN' for user in response.json())
