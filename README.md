# Luizalabs Backend - 2ª Edição (FastAPI) 🚀

Este projeto é uma API robusta para gerenciamento de posts, desenvolvida durante a 2ª Edição do treinamento de Python da Luizalabs. A aplicação foca em **Segurança**, **Arquitetura Limpa** e **Testes Automatizados**.

## 🛠️ Tecnologias Utilizadas

* **FastAPI**: Framework moderno e de alta performance.
* **SQLAlchemy & Databases**: Persistência de dados assíncrona.
* **Pydantic**: Validação de dados e Schemas (Views).
* **JWT (Jose)**: Autenticação segura via tokens.
* **Pytest**: Suíte de testes com 100% de cobertura nos fluxos principais.
* **Poetry**: Gerenciamento de dependências.

## 🔒 Segurança e Configuração

O projeto utiliza variáveis de ambiente para proteger dados sensíveis.
1.  Copie o arquivo `.env.example` para um novo arquivo chamado `.env`.
2.  Preencha as chaves `SECRET_KEY` e as credenciais de teste.

## 🧪 Como rodar os testes

Garanta que o seu ambiente virtual esteja ativo e execute:
```powershell
$env:PYTHONPATH = "."
pytest -v
```

## Como iniciar a API
```powershell
uvicorn app.main:app --reload
```

### Acesse a documentação interativa em: http://127.0.0.1:8000/docs