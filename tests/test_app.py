# tests/test_app.py

import pytest
from app import app # Ganti 'app' dengan nama variabel Flask Anda

@pytest.fixture
def client():
    """Membuat instance test client untuk aplikasi Flask."""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_unauthenticated_home_access(client):
    """
    Tes untuk memastikan pengguna yang BELUM LOGIN akan
    di-redirect ke halaman login saat mengakses halaman utama.
    """
    # Mengirim permintaan GET ke halaman utama ('/')
    response = client.get('/')
    
    # Memastikan respons yang diterima adalah '302 Redirect'
    assert response.status_code == 302
    
    # Memastikan pengguna di-redirect ke URL yang mengandung '/login'
    assert '/login' in response.location

def test_login_page_loads(client):
    """
    Tes untuk memastikan halaman /login itu sendiri dapat diakses
    dan menampilkan konten yang benar.
    """
    response = client.get('/login')
    
    # Memastikan halaman login berhasil diakses (bukan redirect)
    assert response.status_code == 200
    
    # Pastikan ada teks yang seharusnya ada di halaman login Anda
    # Ganti b'Please Sign In' dengan teks yang sesuai.
    assert b'Please Sign In' in response.data
