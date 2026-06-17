from fastapi import FastAPI

from app.config.settings import settings
from app.config.init_db import create_tables

from app.routes.user_routes import router as user_router
from app.routes.aluno_routes import router as aluno_router
from app.routes.professor_routes import router as professor_router
from app.routes.coordenador_routes import router as coordenador_router
from app.routes.empresa_routes import router as empresa_router


create_tables()

app = FastAPI(
    title=settings.PROJECT_NAME,
    description="API do backend para o ecossistema PROJETA",
    version="1.0.0"
)


app.include_router(user_router)
app.include_router(aluno_router)
app.include_router(professor_router)
app.include_router(coordenador_router)
app.include_router(empresa_router)



@app.get("/")
def read_root():
    return {
        "status": "Online",
        "projeto": settings.PROJECT_NAME,
        "mensagem": "Backend inicializado com sucesso!"
    }
