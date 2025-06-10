# tests/test_app.py

import pytest
from app import app # Ganti 'app' dengan nama variabel Flask Anda di file utama

@pytest.fixture
def client():
    """Membuat instance test client untuk aplikasi Flask."""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_page(client):
    """
    Tes untuk memastikan halaman utama dapat diakses (HTTP status code 200).
    """
    # Mengirim permintaan GET ke halaman utama ('/')
    response = client.get('/')
    
    # Memastikan respons yang diterima adalah '200 OK'
    assert response.status_code == 200

def test_home_page_content(client):
    """
    Tes untuk memastikan halaman utama mengandung teks tertentu.
    Ganti b'Hello, World!' dengan teks yang ada di halaman Anda.
    """
    response = client.get('/')
    assert b'Hello, World!' in response.data
