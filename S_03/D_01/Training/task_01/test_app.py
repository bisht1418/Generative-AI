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


def test_add_weather(client):
    response = client.post(
        '/weather', json={'city': 'Chicago', 'temperature': 18, 'weather': 'Sunny'})
    data = response.get_json()

    assert response.status_code == 201
    assert data['message'] == 'Weather data added successfully'


def test_update_weather(client):
    response = client.put('/weather/San Francisco', json={'temperature': 16})
    data = response.get_json()

    assert response.status_code == 200
    assert data['message'] == 'Weather data updated successfully'
    assert app.weather_data['San Francisco']['temperature'] == 16


def test_delete_weather(client):
    response = client.delete('/weather/Seattle')
    data = response.get_json()

    assert response.status_code == 200
    assert data['message'] == 'Weather data deleted successfully'
    assert 'Seattle' not in app.weather_data
