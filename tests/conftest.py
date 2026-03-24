import pytest
from app.main import app
from app.models.post import database
from app.auth import criar_token_acesso
from httpx import ASGITransport, AsyncClient  


@pytest.fixture(autouse=True)
async def gerenciar_banco():
    # Antes do teste: Conecta ao banco
    await database.connect()
    
    yield
    # Depois do teste: Desconecta
    await database.disconnect()


@pytest.fixture
async def cliente():
    # Cria um cliente HTTP assíncrono para os testes
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        yield ac

@pytest.fixture
async def cliente_logado(cliente):
    # Geramos um token válido para o usuário 'guilherme'
    token = criar_token_acesso(dados={"sub": "guilherme"})
    # Injetamos o token no cabeçalho do cliente
    cliente.headers.update({"Authorization": f"Bearer {token}"})
    yield cliente