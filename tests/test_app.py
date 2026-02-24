"""Tests for coordination-drill-live-e2e-r03"""
import pytest
from app import app, drill_state

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

@pytest.fixture(autouse=True)
def reset_state():
    """Reset drill state before each test"""
    drill_state['counter'] = 0
    drill_state['history'] = []
    yield
    drill_state['counter'] = 0
    drill_state['history'] = []

def test_index(client):
    response = client.get('/')
    assert response.status_code == 200
    data = response.get_json()
    assert data['status'] == 'ok'
    assert data['service'] == 'coordination-drill-live-e2e-r03'

def test_health(client):
    response = client.get('/health')
    assert response.status_code == 200
    data = response.get_json()
    assert data['health'] == 'healthy'

def test_drill_get(client):
    response = client.get('/drill')
    assert response.status_code == 200
    data = response.get_json()
    assert data['counter'] == 0
    assert data['history'] == []

def test_drill_post(client):
    response = client.post('/drill')
    assert response.status_code == 200
    data = response.get_json()
    assert data['counter'] == 1
    assert data['action'] == 'incremented'

def test_drill_multiple(client):
    client.post('/drill')
    client.post('/drill')
    response = client.post('/drill')
    data = response.get_json()
    assert data['counter'] == 3

def test_drill_reset(client):
    client.post('/drill')
    client.post('/drill')
    response = client.post('/drill/reset')
    assert response.status_code == 200
    data = response.get_json()
    assert data['counter'] == 0
    assert data['status'] == 'reset'