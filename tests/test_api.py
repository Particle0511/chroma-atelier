import pytest
from backend.app import create_app

@pytest.fixture
def client():
    app = create_app('testing')
    with app.test_client() as client:
        yield client

def test_home_page(client):
    response = client.get('/')
    assert response.status_code == 200

def test_generate_palette(client):
    response = client.post('/generate', json={'query': 'forest'})
    assert response.status_code == 200
    data = response.get_json()
    assert 'colors' in data
    assert len(data['colors']) == 5
    assert 'hex' in data['colors'][0]

def test_missing_query(client):
    response = client.post('/generate', json={})
    assert response.status_code == 400