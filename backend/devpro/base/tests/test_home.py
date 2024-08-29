def test_home_status(client):
    resp = client.get('/')
    assert resp.status_code == 200
