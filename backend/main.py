from os import name
from fastapi import FastAPI
from core.config import settings
from db.session import engine
from db.base import Base
from apis.base import api_router
from webapps.base import api_router as webapp_router
from fastapi.staticfiles import StaticFiles


def create_tables():
    Base.metadata.create_all(bind=engine)

    
def include_router(app):
    app.include_router(api_router)    # добавляем список маршрутов для API
    app.include_router(webapp_router) # добавляем список маршрутов для web


def configure_static(app):
    app.mount("/staic", StaticFiles(directory="static"),name="static")


def satrt_application():
    app = FastAPI(title=settings.PROJECT_TITLE, version=settings.PROJECT_VERSION)
    create_tables()     # создаем таблици при запуске приложения
    include_router(app) # добавляем маршруты
    configure_static(app) # создаем директорию для хранения статических файлов
    return app


app = satrt_application()

# @app.get("/")
# def hello_api():
#     return {"detail":"Hello Wold!"}