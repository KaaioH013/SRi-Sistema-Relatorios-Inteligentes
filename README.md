# 🧠 SRi – Sistema de Relatórios Inteligentes

Um projeto Full Stack didático, desenvolvido passo a passo com o mentor 'Parceiro de Programação', focado em criar um sistema de relatórios completo e profissional para fins de portfólio.

## 🚀 Stack Tecnológica

| Componente | Tecnologia | Observação |
| :--- | :--- | :--- |
| **Backend** | FastAPI (Python) | API rápida e moderna. |
| **Frontend** | React (Vite) | Interface de usuário dinâmica. |
| **Banco de Dados**| SQLite/PostgreSQL | SQLite (local, gratuito) e PostgreSQL (deploy). |
| **Deploy** | Railway (Backend) & Vercel (Frontend) | Plataformas gratuitas para o deploy. |

## ⚙️ Instruções de Instalação e Execução

### 1. Backend (FastAPI)

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/KaaioH013/SRi-Sistema-Relatorios-Inteligentes.git](https://github.com/KaaioH013/SRi-Sistema-Relatorios-Inteligentes.git)
    cd SRi-Sistema-Relatorios-Inteligentes/backend
    ```
2.  **Crie e Ative o Ambiente Virtual:**
    ```bash
    python -m venv venv
    # Linux/Mac
    source venv/bin/activate
    # Windows (CMD)
    # venv\Scripts\activate
    ```
3.  **Instale as Dependências:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Execute o Servidor:**
    ```bash
    uvicorn main:app --reload
    ```
    O servidor estará acessível em `http://127.0.0.1:8000`.

## 🧭 Roadmap de Desenvolvimento

| Etapa | Descrição | Status |
| :--- | :--- | :--- |
| **🏁 Etapa 1** | **Setup Inicial do Ambiente** | ✅ CONCLUÍDA |
| ⚙️ Etapa 2 | Backend: API Base | ⏳ Pendente |
| 🧱 Etapa 3 | Banco de Dados | ❌ |
| 🔐 Etapa 4 | Autenticação JWT | ❌ |
| 🎨 Etapa 5 | Frontend (React) Setup | ❌ |
| 📊 Etapa 6 | Dashboard e Relatórios | ❌ |
| 📂 Etapa 7 | Deploy Gratuito | ❌ |
| 🧾 Etapa 8 | Documentação Final | ❌ |