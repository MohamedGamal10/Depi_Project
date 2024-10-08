import pytest
from mederpapp import app  # Assuming depi_app.py is the main app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_homepage(client):
    """Test if the homepage is accessible"""
    rv = client.get('/')
    assert rv.status_code == 200

def test_database_connection():
    """Test database connection"""
    # Example test for database connection (adjust according to your actual DB setup)
    from connectsql import connect_db
    connection = connect_db()
    assert connection is not None