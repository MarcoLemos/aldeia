from fastapi.testclient import TestClient

from aldeia.main import app

client = TestClient(app)


def test_new_pessoa():
    response = client.post('/pessoas', 
    json={
            "nome": "Foo"
        },
    )
    assert response.status_code == 200
    assert isinstance(response.json(), dict)
    if response.json():
        assert isinstance(response.json()['nome'], str)

def test_read_item():
    response = client.get('/pessoas')
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    if response.json():
        assert isinstance(response.json()[0]['nome'], str)


