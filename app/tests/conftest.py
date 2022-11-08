import pytest
from app import db
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True  
    app.config['WTF_CSRF_ENABLED'] = False
    with app.test_client() as client:
      with app.app_context():
        yield client

@pytest.fixture
def session(): # 1
    connection = db.connect(':memory:')
    db_session = connection.cursor()
    yield db_session
    connection.close()
