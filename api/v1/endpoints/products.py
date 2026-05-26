from typing import List
from fastapi import APIRouter, HTTPException, status

from schemas.product import (
    ProductCreate,
    ProductUpdate,
    ProductOut
)

# Base de datos simulada
productos = [
    {
        "id": 1,
        "nombre": "Mouse Gamer",
        "stock": 10,
        "precio": 80000
    },
    {
        "id": 2,
        "nombre": "Teclado Mecánico",
        "stock": 5,
        "precio": 150000
    }
]

# Crear router
router = APIRouter()

# Obtener todos los productos
@router.get("/", response_model=List[ProductOut])
async def obtener_productos():
    return productos

# Obtener producto por ID
@router.get("/{id}", response_model=ProductOut)
async def obtener_producto(id: int):

    producto = next((p for p in productos if p["id"] == id), None)

    if not producto:
        raise HTTPException(
            status_code=404,
            detail="Producto no encontrado"
        )

    return producto

# Crear producto
@router.post(
    "/",
    response_model=ProductOut,
    status_code=status.HTTP_201_CREATED
)
async def crear_producto(new_product: ProductCreate):

    nuevo_id = max(p["id"] for p in productos) + 1 if productos else 1

    nuevo_producto = {
        **new_product.model_dump(),
        "id": nuevo_id
    }

    productos.append(nuevo_producto)

    return nuevo_producto

# Actualizar producto
@router.put("/{id}", response_model=ProductOut)
async def actualizar_producto(id: int, producto: ProductUpdate):

    for i, p in enumerate(productos):

        if p["id"] == id:

            update_data = producto.model_dump(exclude_unset=True)

            productos[i].update(update_data)

            return productos[i]

    raise HTTPException(
        status_code=404,
        detail="Producto no encontrado"
    )

# Eliminar producto
@router.delete(
    "/{id}",
    status_code=status.HTTP_204_NO_CONTENT
)
async def eliminar_producto(id: int):

    for i, p in enumerate(productos):

        if p["id"] == id:

            productos.pop(i)

            return

    raise HTTPException(
        status_code=404,
        detail="Producto no encontrado"
    )