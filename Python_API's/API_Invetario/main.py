from fastapi import FastAPI
from routes.usuario_routes import router

app = FastAPI()

app.include_router(router)
