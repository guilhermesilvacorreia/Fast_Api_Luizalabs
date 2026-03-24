import pytest

@pytest.mark.asyncio
async def test_deletar_post_com_sucesso(cliente_logado):
    # 1. Primeiro criamos um post para ter o que deletar
    novo_post = {"titulo": "Post para Deletar", "conteudo": "...", "categoria": "teste"}
    res_create = await cliente_logado.post("/posts/", json=novo_post)
    post_id = res_create.json()["id"]

    # 2. Agora o 'cliente_logado' já tem o token, basta deletar!
    response = await cliente_logado.delete(f"/posts/{post_id}")
    
    assert response.status_code == 204

@pytest.mark.asyncio
async def test_filtrar_posts_por_categoria(cliente_logado):
    # 1. Criamos dois posts de categorias diferentes
    await cliente_logado.post("/posts/", json={
        "titulo": "Post Python", "conteudo": "...", "categoria": "python"
    })
    await cliente_logado.post("/posts/", json={
        "titulo": "Post Java", "conteudo": "...", "categoria": "java"
    })

    # 2. Fazemos a busca filtrando apenas por 'python'
    response = await cliente_logado.get("/posts/?categoria=python")
    
    # 3. Verificamos se só veio 1 post e se a categoria está correta
    dados = response.json()
    assert response.status_code == 200
    assert len(dados) >= 1
    assert all (d["categoria"] == "python" for d in dados)