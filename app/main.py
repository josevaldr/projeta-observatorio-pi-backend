from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config.settings import settings
from app.config.init_db import create_tables

from app.routes.user_routes import router as user_router
from app.routes.aluno_routes import router as aluno_router
from app.routes.professor_routes import router as professor_router
from app.routes.coordenador_routes import router as coordenador_router
from app.routes.empresa_routes import router as empresa_router
from app.routes.projeto_routes import router as projeto_router
from app.routes.equipe_routes import router as equipe_router
from app.routes.avaliacao_routes import router as avaliacao_router
from app.routes.estatisticas_routes import router as estatisticas_router

create_tables()

app = FastAPI(
    title=settings.PROJECT_NAME,
    description="API do backend para o ecossistema PROJETA",
    version="1.0.0"
)

origins = [
    "http://localhost:8000",
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(user_router)
app.include_router(aluno_router)
app.include_router(professor_router)
app.include_router(coordenador_router)
app.include_router(empresa_router)
app.include_router(projeto_router)
app.include_router(equipe_router)
app.include_router(avaliacao_router)
app.include_router(estatisticas_router)

@app.get("/")
def read_root():
    return {
        "status": "Online",
        "projeto": settings.PROJECT_NAME,
        "mensagem": "Backend inicializado com sucesso!"
    }
