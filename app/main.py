from fastapi import FastAPI
from app.models import Transaccion

app = FastAPI(title="API de Finanzas Personales")

# 1. Simulamos una base de datos en memoria con una lista vacía
base_de_datos = []

@app.get("/")
def ruta_principal():
    return {"mensaje": "¡Hola! Mi API de finanzas está funcionando correctamente."}

# 2. NUEVA RUTA GET: Devuelve toda la lista de transacciones
@app.get("/transacciones/")
def obtener_transacciones():
    return base_de_datos

# 3. MODIFICADA: Ahora guardamos el dato en la lista antes de responder
@app.post("/transacciones/")
def registrar_transaccion(transaccion: Transaccion):
    base_de_datos.append(transaccion) # Añadimos el dato a la lista
    return {
        "mensaje": "Transacción registrada con éxito",
        "transaccion": transaccion
    }