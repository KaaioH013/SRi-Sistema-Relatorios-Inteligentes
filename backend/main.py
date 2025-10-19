from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
# --- IMPORTAÇÕES DO BANCO ---
import models 
from database import engine 
# --- IMPORTAÇÕES DO ROUTER (CORREÇÃO AQUI) ---
# Importa o módulo users *diretamente* do arquivo users.py
from routers.users import router as users_router
# Importa o módulo reports *diretamente* do arquivo reports.py
from routers.reports import router as reports_router 
# --- FIM DAS CORREÇÕES ---


# CRIAÇÃO DAS TABELAS NO BANCO DE DADOS (Executado uma única vez)
models.Base.metadata.create_all(bind=engine) 

# 1. Cria a instância principal do aplicativo FastAPI
app = FastAPI(
    title="SRi - Sistema de Relatórios Inteligentes API",
    version="1.0.0",
    description="Backend em FastAPI para o Sistema de Relatórios Inteligentes (SRi)."
)

# 2. Configuração do CORS (Cross-Origin Resource Sharing)
origins = [
    "http://localhost",
    "http://localhost:3000",
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins, 
    allow_credentials=True, 
    allow_methods=["*"], 
    allow_headers=["*"], 
)

# 3. Inclusão dos Roteadores (CORREÇÃO AQUI)
# Usamos o 'users_router' e 'reports_router' que definimos na importação.
app.include_router(users_router, prefix="/api/v1/users", tags=["Usuários"])
app.include_router(reports_router, prefix="/api/v1/reports", tags=["Relatórios"])

# 4. Rota Raiz (Hello World, mantida para teste de saúde)
@app.get("/", tags=["Status"])
def read_root():
    return {"message": "SRi Backend está no ar!", "status": "Online"}

# 5. Rota de Status (Também mantida)
@app.get("/status", tags=["Status"])
def get_status():
    return {"status": "online", "service": "SRi API", "version": "1.0.0"}