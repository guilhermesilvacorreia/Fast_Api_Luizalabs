import pytest
import os  
from dotenv import load_dotenv
load_dotenv()

@pytest.mark.asyncio
async def test_login_sucesso_deve_retornar_token(cliente):
    # Em vez de escrever o texto, pegamos do ambiente
    dados_login = {
        "username": os.getenv("TEST_USER", "guilherme"),
        "password": os.getenv("TEST_PASSWORD", "123456")
    }
    response = await cliente.post("/token", data=dados_login)
    
    assert response.status_code == 200
    assert "access_token" in response.json()

@pytest.mark.asyncio
async def test_login_falha_senha_errada(cliente):
    dados_login = {"username": "guilherme", "password": "senha_errada"}
    response = await cliente.post("/token", data=dados_login)
    
    assert response.status_code == 401
    assert response.json()["detail"] == "Usuário ou senha incorretos"

@pytest.mark.asyncio
async def test_deletar_sem_token_deve_dar_erro_401(cliente):
    # Tentamos deletar qualquer ID sem passar o Header de Authorization
    response = await cliente.delete("/posts/99")
    assert response.status_code == 401