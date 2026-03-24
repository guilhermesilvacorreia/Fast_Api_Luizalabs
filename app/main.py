from contextlib import asynccontextmanager
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from app.auth import criar_token_acesso, obter_usuario_atual

from app.controllers.post_controller import router as post_router
from app.models.post import database 

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Conecta ao banco no início
    await database.connect()
    yield 
    # Desconecta ao desligar
    await database.disconnect()

# Criamos a instância APENAS UMA VEZ com todas as configurações
app = FastAPI(title="Luizalabs Backend - Protegido", lifespan=lifespan)

@app.post("/token", tags=["Autenticação"])
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    # Simulação de verificação
    if form_data.username == "guilherme" and form_data.password == "123456":
        token = criar_token_acesso(dados={"sub": form_data.username})
        return {"access_token": token, "token_type": "bearer"}
    
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Usuário ou senha incorretos",
        headers={"WWW-Authenticate": "Bearer"},
    )

# Incluímos as rotas de posts
app.include_router(post_router)

@app.get("/", tags=["Status"])
def home():
    return {"status": "Online"}
