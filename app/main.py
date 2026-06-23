from fastapi import FastAPI
from app.models import Transaccion # Importamos el modelo desde nuestro nuevo archivo

app = FastAPI(title="API de Finanzas Personales")

@app.get("/")
def ruta_principal():
    return {"mensaje": "¡Hola! Mi API de finanzas está funcionando correctamente."}

@app.post("/transacciones/")
def registrar_transaccion(transaccion: Transaccion):
    return {
        "mensaje": "Transacción registrada con éxito",
        "datos_recibidos": transaccion
    }