from fastapi import APIRouter, HTTPException, status, Depends
from app.auth import obter_usuario_atual
from typing import List, Optional
from app.models.post import database, posts 
from app.views.post_view import PostSchema as PostCreate, PostPublic

router = APIRouter(prefix="/posts", tags=["Posts"])

# CREATE - Apenas usuários logados podem criar
@router.post("/", response_model=PostPublic, status_code=status.HTTP_201_CREATED)
async def criar_post(post: PostCreate, usuario: str = Depends(obter_usuario_atual)):
    query = posts.insert().values(
        titulo=post.titulo, 
        conteudo=post.conteudo, 
        publicado=post.publicado,
        categoria=post.categoria
    )
    last_record_id = await database.execute(query)
    return {**post.model_dump(), "id": last_record_id}

# READ (ALL) - Público (Qualquer um pode ler)
@router.get("/", response_model=List[PostPublic])
async def listar_posts(categoria: Optional[str] = None):
    query = posts.select()
    if categoria:
        query = query.where(posts.c.categoria == categoria)
    return await database.fetch_all(query)

# READ (ONE) - Público
@router.get("/{post_id}", response_model=PostPublic)
async def buscar_post(post_id: int):
    query = posts.select().where(posts.c.id == post_id)
    post = await database.fetch_one(query)
    if not post:
        raise HTTPException(status_code=404, detail="Post não encontrado")
    return post

# UPDATE - Apenas usuários logados podem atualizar
@router.put("/{post_id}", response_model=PostPublic)
async def atualizar_post(post_id: int, post_atualizado: PostCreate, usuario: str = Depends(obter_usuario_atual)):
    query_check = posts.select().where(posts.c.id == post_id)
    exists = await database.fetch_one(query_check)
    
    if not exists:
        raise HTTPException(status_code=404, detail="Post não existe para atualizar")

    query = posts.update().where(posts.c.id == post_id).values(
        titulo=post_atualizado.titulo,
        conteudo=post_atualizado.conteudo,
        publicado=post_atualizado.publicado,
        categoria=post_atualizado.categoria
    )
    await database.execute(query)
    return {**post_atualizado.model_dump(), "id": post_id}

# DELETE - Apenas usuários logados podem deletar
@router.delete("/{post_id}", status_code=status.HTTP_204_NO_CONTENT)
async def deletar_post(post_id: int, usuario: str = Depends(obter_usuario_atual)):
    query = posts.delete().where(posts.c.id == post_id)
    result = await database.execute(query)
    
    if result == 0:
        raise HTTPException(status_code=404, detail="Post não encontrado para deletar")
    return None