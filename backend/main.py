from fastapi import FastAPI
from core.config import settings
from db.session import engine
from db.base import Base


def create_tables():
    Base.metadata.create_all(bind=engine)

def satrt_application():
    app = FastAPI(title=settings.PROJECT_TITLE, version=settings.PROJECT_VERSION)
    create_tables()
    return app

app = satrt_application()

@app.get("/")
def hello_api():
    return {"detail":"Hello Wold!"}