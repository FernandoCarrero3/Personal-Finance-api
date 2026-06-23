from pydantic import BaseModel, Field
from uuid import UUID, uuid4
from datetime import datetime

class Transaccion(BaseModel):
    # Field(default_factory=...) autogenera el valor en el momento de crear el registro
    id: UUID = Field(default_factory=uuid4, description="Identificador único de la transacción")
    concepto: str
    cantidad: float
    categoria: str = "Sin clasificar"
    fecha: datetime = Field(default_factory=datetime.now, description="Fecha y hora del registro")