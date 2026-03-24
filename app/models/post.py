import databases
import sqlalchemy
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./test.db")

database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()

# Definição ÚNICA da tabela de Posts
posts = sqlalchemy.Table(
    "posts",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("titulo", sqlalchemy.String),
    sqlalchemy.Column("conteudo", sqlalchemy.String),
    sqlalchemy.Column("publicado", sqlalchemy.Boolean),
    sqlalchemy.Column("categoria", sqlalchemy.String),  
)

engine = sqlalchemy.create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)

 
metadata.create_all(engine)

# Classe de domínio (opcional)
class Post:
    def __init__(self, id: int, titulo: str, conteudo: str, categoria: str, publicado: bool = True):
        self.id = id
        self.titulo = titulo
        self.conteudo = conteudo
        self.categoria = categoria
        self.publicado = publicado