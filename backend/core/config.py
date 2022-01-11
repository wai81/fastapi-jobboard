import os
from pathlib import Path
from dotenv import load_dotenv

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)


class Setings:
    # заголовок API
    PROJECT_TITLE:   str = "Jobboard"
    PROJECT_VERSION: str = "0.1.1"
    
    # подключения к базе
    POSTGRES_USER:      str = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD:  str = os.getenv("POSTGRES_PASSWORD")
    POSTGRES_SERVER:    str = os.getenv("POSTGRES_SERVER","localhost")
    POSTGRES_PORT:      str = os.getenv("POSTGRES_PORT",5432) # default postgres port is 5432
    POSTGRES_DB:        str = os.getenv("POSTGRES_DB","db_joddoard")
    DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"
    
    # настройки ключа JWT
    SECRET_KEY:str = os.getenv("SECRET_KEY")
    ALGORITHM ="HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 30
    
    TEST_USER_EMAIL = "test@example.com" 
    
settings = Setings()