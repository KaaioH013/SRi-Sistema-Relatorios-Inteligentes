from fastapi import APIRouter

# Novamente, não precisamos de importações de 'models' ou 'database' aqui AINDA.

router = APIRouter()

@router.get("/")
async def list_reports():
    fake_reports = [
        {"id": 101, "title": "Relatório de Vendas Mensais", "status": "Concluído"},
        {"id": 102, "title": "Relatório de Estoque Crítico", "status": "Processando"},
    ]
    return fake_reports

@router.post("/generate")
async def generate_report():
    return {"message": "Relatório gerado em segundo plano (FAKE)!"}

@router.get("/{report_id}/download")
async def download_report(report_id: int):
    return {"message": f"Preparando download do Relatório {report_id}", "report_id": report_id}