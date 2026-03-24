import pytest

@pytest.mark.asyncio
async def test_home_deve_retornar_online(cliente):
    response = await cliente.get("/")
    assert response.status_code == 200
    assert response.json() == {"status": "Online"}

@pytest.mark.asyncio
async def test_listar_posts_status_200(cliente):
    response = await cliente.get("/posts/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    