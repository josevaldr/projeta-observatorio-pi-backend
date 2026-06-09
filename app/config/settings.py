import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    PROJECT_NAME: str = "Observatório de Projetos Integradores - PROJETA"
    SECRET_KEY: str = os.getenv("SECRET_KEY", "chave-provisoria-super-segura")
    
settings = Settings()