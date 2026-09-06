# Projeto Athena (version.1.beta)

Plataforma inicial de apoio à organização, rotina e recursos para pessoas neurodivergentes.

> Este projeto é um protótipo educacional. Não substitui avaliação, diagnóstico ou tratamento profissional.

## Stack
- FastAPI + SQLAlchemy
- PostgreSQL
- JWT
- Alembic
- Streamlit
- Docker Compose

## Executar
1. Copie `.env.example` para `.env`.
2. Execute `docker compose up --build`.
3. API: http://localhost:8000/docs
4. Frontend: http://localhost:8501

A primeira execução aplica as migrações do Alembic automaticamente.
