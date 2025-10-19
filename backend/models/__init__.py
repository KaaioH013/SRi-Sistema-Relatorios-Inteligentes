from sqlalchemy import Column, Integer, String, Boolean, DateTime, Text, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

# Importa a Base que definimos no database.py. O ".." indica que deve subir uma pasta
# (sair de models/ para backend/) e procurar o database.py.
from database import Base 

# =========================================================
# Modelo: Usuário (Tabela 'users')
# =========================================================
class User(Base):
    # Nome da Tabela no Banco
    __tablename__ = "users"

    # Colunas da Tabela
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False) 
    is_active = Column(Boolean, default=True)
    is_admin = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    # Relacionamento: Liga este usuário aos relatórios que ele criou.
    relatorios = relationship("Report", back_populates="owner")
    
# =========================================================
# Modelo: Relatório (Tabela 'reports')
# =========================================================
class Report(Base):
    # Nome da Tabela no Banco
    __tablename__ = "reports"

    # Colunas da Tabela
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True, nullable=False)
    description = Column(Text, nullable=True) 
    status = Column(String, default="Pendente")
    
    # Chave Estrangeira: A coluna que liga o relatório ao seu criador (o usuário).
    owner_id = Column(Integer, ForeignKey("users.id"))
    
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Relacionamento: Permite acessar o objeto User (o dono) a partir do Report.
    owner = relationship("User", back_populates="relatorios")


# Documentação:
# - `ForeignKey("users.id")`: Informa que esta coluna deve referenciar a coluna `id` da tabela `users`.
# - A herança de `Base` é o que diz ao SQLAlchemy: "Esta classe é uma tabela!"