from fastapi import FastAPI
from app.routers import transacciones # Importamos nuestro router

app = FastAPI(title="API de Finanzas Personales")

# Conectamos el router a la aplicación principal
app.include_router(transacciones.router)

@app.get("/")
def ruta_principal():
    return {"mensaje": "¡Hola! Mi API de finanzas está funcionando correctamente."}