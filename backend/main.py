from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
# Iremos importar os roteadores que criaremos no próximo passo
# from .routers import users, reports # Ainda não existem, mas vamos prepará-los!

# 1. Cria a instância principal do aplicativo FastAPI
app = FastAPI(
    title="SRi - Sistema de Relatórios Inteligentes API",
    version="1.0.0",
    description="Backend em FastAPI para o Sistema de Relatórios Inteligentes (SRi)."
)

# 2. Configuração do CORS (Cross-Origin Resource Sharing)
# Permite que nosso Frontend React (rodando em outra porta) se comunique com esta API.
origins = [
    # Permitir o acesso do frontend em desenvolvimento local (porta padrão do Vite/React)
    "http://localhost",
    "http://localhost:3000",
    "http://localhost:5173",
    # Adicione aqui o domínio de produção no futuro (ex: 'https://sri-frontend.vercel.app')
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins, # Lista de origens permitidas
    allow_credentials=True, # Permitir cookies e cabeçalhos de autorização
    allow_methods=["*"], # Permitir todos os métodos (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"], # Permitir todos os cabeçalhos
)

# 3. Inclusão dos Roteadores (Comente por enquanto, vamos criá-los no próximo passo)
# app.include_router(users.router, prefix="/api/v1/users", tags=["Usuários"])
# app.include_router(reports.router, prefix="/api/v1/reports", tags=["Relatórios"])

# 4. Rota Raiz (Hello World, mantida para teste de saúde)
@app.get("/", tags=["Status"])
def read_root():
    return {"message": "SRi Backend está no ar!", "status": "Online"}

# 5. Rota de Status (Também mantida)
@app.get("/status", tags=["Status"])
def get_status():
    return {"status": "online", "service": "SRi API", "version": "1.0.0"}


# Documentação:
# - `CORSMiddleware`: É o componente que lida com a segurança de comunicação entre domínios.
# - `allow_origins`: É a lista dos endereços que têm permissão para acessar a API. Colocamos o localhost com portas comuns do React.
# - `prefix="/api/v1/users"`: É a convenção de prefixar as rotas por `/api/v1` (API Version 1) e depois pela funcionalidade (users, reports).