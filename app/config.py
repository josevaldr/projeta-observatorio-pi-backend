import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    PROJECT_NAME: str = "Observatório de Projetos Integradores - PROJETA"
    SECRET_KEY: str = os.getenv("SECRET_KEY", "chave-provisoria-super-segura")
    
    # Credenciais do MySQL que usaremos mais à frente
    DB_HOST: str = os.getenv("DB_HOST", "localhost")
    DB_USER: str = os.getenv("DB_USER", "root")
    DB_PASSWORD: str = os.getenv("DB_PASSWORD", "")
    DB_NAME: str = os.getenv("DB_NAME", "projeta_db")

settings = Settings()