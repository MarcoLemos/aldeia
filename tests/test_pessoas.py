import pytest
from httpx import AsyncClient


@pytest.mark.anyio
async def test_new_pessoa(client: AsyncClient):
    response = await client.post('/pessoas/', 
    json={
            "nome": "Foo"
        },
    )
    assert response.status_code == 200
    assert isinstance(response.json(), dict)
    if response.json():
        assert isinstance(response.json()['nome'], str)

@pytest.mark.anyio
async def test_read_item(client: AsyncClient):
    response = await client.get('/pessoas/')
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    if response.json():
        assert isinstance(response.json()[0]['nome'], str)


