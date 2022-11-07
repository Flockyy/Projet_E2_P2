import pytest
from app import create_app

@pytest.fixture()
def app():
    app = create_app()
    app.config.update({
        "TESTING": True,
    })
    
    yield app


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()
  
@pytest.fixture()
def test_request_example(client):
    response = client.get("/")
    assert b"<h1 class='title'> House Price Prediction in Ames (Iowa)</h1><h2 class='subtitle'>Easy authentication and house price prediction.</h2>" in response.data