from fastapi import FastAPI

# 1. Inicializamos la aplicación (Esto es exactamente igual que hacer "const app = express()" en Node.js)
app = FastAPI(title="API de Finanzas Personales")

# 2. Creamos nuestro primer endpoint (ruta)
# El símbolo "@" se llama "decorador". Sirve para decirle a FastAPI que la función de abajo es una ruta GET.
@app.get("/")
def ruta_principal():
    return {"mensaje": "¡Hola! Mi API de finanzas está funcionando correctamente."}