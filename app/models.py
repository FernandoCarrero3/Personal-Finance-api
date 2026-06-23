from pydantic import BaseModel

# Este es nuestro "Modelo". Define qué forma tiene una transacción financiera.
class Transaccion(BaseModel):
    concepto: str
    cantidad: float
    categoria: str = "Sin clasificar" # Valor por defecto