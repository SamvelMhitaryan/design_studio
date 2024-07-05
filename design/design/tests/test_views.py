import pytest


@pytest.mark.django_db
def test_rate_view(client):
    response = client.get('/api/rates/')
    assert response.status_code == 200


@pytest.mark.django_db
def test_services_view(client):
    response = client.get('/api/services/')
    assert response.status_code == 200
