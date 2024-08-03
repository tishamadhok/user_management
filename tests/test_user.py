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
