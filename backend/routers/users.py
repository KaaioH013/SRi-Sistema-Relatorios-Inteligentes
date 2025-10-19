from fastapi import APIRouter

# Não precisamos de importações de 'models' ou 'database' aqui AINDA.
# As importaremos somente quando formos interagir com o banco de dados.

router = APIRouter()

@router.post("/")
async def create_user():
    return {"message": "Usuário criado com sucesso (FAKE)!"}

@router.get("/")
async def list_users():
    fake_users = [
        {"id": 1, "username": "caioh013", "email": "caio@sri.com"},
        {"id": 2, "username": "admin_sri", "email": "admin@sri.com"},
    ]
    return fake_users

@router.get("/{user_id}")
async def get_user(user_id: int):
    return {"message": f"Detalhes do Usuário {user_id}", "user_id": user_id}