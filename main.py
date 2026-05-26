from fastapi import FastAPI
from api.v1.api import api_router

app = FastAPI(
    title="Mi Primera API",
    description="API de ejemplo para tienda",
    version="1.0.0"
)

@app.get("/")
async def root():
    return {"mensaje": "Bienvenido a mi API"}

# Conectar rutas
app.include_router(
    api_router,
    prefix="/api/v1"
)