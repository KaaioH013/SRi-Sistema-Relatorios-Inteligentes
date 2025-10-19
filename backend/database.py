from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# URL que aponta para o arquivo SQLite. Ele será criado na raiz do projeto (..)
# O ".." serve para sair da pasta backend/ e salvar na pasta principal do projeto
SQLALCHEMY_DATABASE_URL = "sqlite:///../sri_database.db"

# Criação do Engine (Motor de Conexão)
# O `check_same_thread: False` é EXCLUSIVO para SQLite, permitindo que o FastAPI funcione
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# Criação da Classe Base: Todos os nossos modelos de tabela herdarão desta classe.
Base = declarative_base()

# Criação da Sessão Local: Usada para criar sessões de leitura/escrita no banco.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Documentação:
# - `SQLALCHEMY_DATABASE_URL`: Define o tipo de banco (sqlite) e o nome do arquivo (`sri_database.db`).
# - `engine`: Gerencia a comunicação de baixo nível com o arquivo.
# - `Base`: É a fundação para a criação das tabelas.