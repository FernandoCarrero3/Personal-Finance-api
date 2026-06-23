import json
import os
from app.models import Transaccion

# Ruta donde se guardará nuestro archivo (en la raíz del proyecto)
ARCHIVO_DB = "datos.json"

def cargar_transacciones() -> list[Transaccion]:
    """Lee el archivo JSON y devuelve una lista de objetos Transaccion."""
    # Si el archivo no existe (la primera vez), devolvemos una lista vacía
    if not os.path.exists(ARCHIVO_DB):
        return []
        
    with open(ARCHIVO_DB, "r", encoding="utf-8") as f:
        datos = json.load(f)
        # Convertimos los diccionarios de vuelta a nuestros modelos Pydantic
        return [Transaccion(**item) for item in datos]

def guardar_transacciones(transacciones: list[Transaccion]):
    """Recibe una lista de Transacciones y las guarda en el archivo JSON."""
    with open(ARCHIVO_DB, "w", encoding="utf-8") as f:
        # Convertimos los objetos a formato JSON compatible
        datos_json = [t.model_dump(mode='json') for t in transacciones]
        # Guardamos en el archivo con indentación para que sea legible
        json.dump(datos_json, f, indent=4, ensure_ascii=False)