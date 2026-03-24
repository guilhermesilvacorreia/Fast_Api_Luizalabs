from datetime import datetime, timedelta, timezone
from jose import JWTError, jwt
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
import os
from dotenv import load_dotenv

load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")  
ALGORITHM = os.getenv("ALGORITHM", "HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 30))
 
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def criar_token_acesso(dados: dict):
    dados_copia = dados.copy()
    expira = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    dados_copia.update({"exp": expira})
    return jwt.encode(dados_copia, SECRET_KEY, algorithm=ALGORITHM)

# Esta função será usada como "Cadeado" nas rotas
async def obter_usuario_atual(token: str = Depends(oauth2_scheme)):
    erro_autenticacao = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Credenciais inválidas ou expiradas",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise erro_autenticacao
        return username
    except JWTError:
        raise erro_autenticacao