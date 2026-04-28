from fastapi import FastAPI

app = FastAPI(
    title="Mi Primera API",
    description="API de ejemplo para",
    version="1.0.0"
)

@app.get("/")
async def root() :
    """Endpoind raiz que retorna saludo."""
    return {"mensaje":"hola fastAPI"}

@app.get("/saludar/{nombre}")
def saludar(nombre: str):
    """ Endpoint que saluda a la persona cuyo nombre se porporciona en la ruta"""
    if nombre in "jennifer":
        return{"mensage": f"hola,{nombre}"}
    