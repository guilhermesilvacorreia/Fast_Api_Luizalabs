from pydantic import BaseModel, Field
from typing import Optional

# 1. Este é o molde para quem ENVIA dados (POST/PUT)
class PostSchema(BaseModel):
    titulo: str = Field(..., min_length=3, max_length=50)
    conteudo: str
    publicado: bool = True
    categoria: Optional[str] = None

# 2. Este é o molde para quem RECEBE dados (GET)
# Ele herda TUDO do PostSchema e adiciona o ID
class PostPublic(PostSchema):
    id: int