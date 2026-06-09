from fastapi import FastAPI
from app.config.settings import settings

app = FastAPI(
    title=settings.PROJECT_NAME,
    description="API do backend para o ecossistema PROJETA",
    version="1.0.0"
)

@app.get("/")
def read_root():
    return {
        "status": "Online",
        "projeto": settings.PROJECT_NAME,
        "mensagem": "Backend inicializado com sucesso!"
    }

# 🛠️ ADICIONE ESTAS LINHAS ABAIXO NO FINAL DO FICHEIRO:
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)