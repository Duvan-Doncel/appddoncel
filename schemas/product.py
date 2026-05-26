from pydantic import BaseModel, Field
from typing import Optional

# Esquema base
class ProductBase(BaseModel):
    nombre: str = Field(..., min_length=3, max_length=70, example="Mouse Gamer")
    stock: int = Field(..., ge=0, example=10)
    precio: float = Field(..., ge=0, example=80000)

# Crear producto
class ProductCreate(ProductBase):
    pass

# Actualizar producto
class ProductUpdate(BaseModel):
    nombre: Optional[str] = Field(None, min_length=3, max_length=70)
    stock: Optional[int] = Field(None, ge=0)
    precio: Optional[float] = Field(None, ge=0)

# Salida del producto
class ProductOut(ProductBase):
    id: int

    class Config:
        from_attributes = True