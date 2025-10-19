from fastapi import FastAPI

# 1. Cria a instância principal do aplicativo FastAPI.
# Esta variável 'app' é o coração do nosso backend e o Uvicorn irá procurá-la.
app = FastAPI()

# 2. Define nossa primeira Rota (Endpoint)
# O decorador '@app.get("/")' diz ao FastAPI:
# "Quando o usuário fizer uma requisição HTTP do tipo GET no endereço raiz ('/'),
# execute a função 'read_root' abaixo."
@app.get("/")
def read_root():
    # O FastAPI automaticamente converte este dicionário Python em uma resposta JSON.
    return {"message": "Hello World! SRi Backend está no ar!"}

# 3. Segunda Rota: Para verificar o status do serviço
@app.get("/status")
def get_status():
    # Isso é útil para verificar a saúde da API.
    return {"status": "online", "service": "SRi API", "version": "1.0.0"}


# Documentação:
# - `from fastapi import FastAPI`: Importamos a classe que constrói a API.
# - `app = FastAPI()`: Inicializamos o aplicativo.
# - `@app.get(...)`: É a forma elegante do Python de mapear URLs para funções.
# - As funções retornam dados que serão enviados ao cliente (navegador, frontend, etc.).