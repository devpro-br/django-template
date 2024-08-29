from django.urls import reverse


def test_login_page_status(client):
    resp = client.get(reverse('login'))
    assert resp.status_code == 200
