import pytest
from app import app


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_get_weather(client):
    response = client.get('/weather/San Francisco')
    data = response.get_json()

    assert response.status_code == 200
    assert data['temperature'] == 14
    assert data['weather'] == 'Cloudy'
