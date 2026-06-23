from fastapi import FastAPI
from app.models import Transaccion

app = FastAPI(title="API de Finanzas Personales")

base_de_datos = []


@app.get("/")
def ruta_principal():
    return {"mensaje": "¡Hola! Mi API de finanzas está funcionando correctamente."}


@app.get("/transacciones/")
def obtener_transacciones():
    return base_de_datos


@app.post("/transacciones/")
def registrar_transaccion(transaccion: Transaccion):
    base_de_datos.append(transaccion)  # Añadimos el dato a la lista
    return {"mensaje": "Transacción registrada con éxito", "transaccion": transaccion}


@app.get("/analiticas/")
def obtener_analiticas():
    # 1. Calculamos el total sumando la "cantidad" de cada transacción
    total_gastos = sum(t.cantidad for t in base_de_datos)

    # 2. Agrupamos los gastos usando un diccionario
    gastos_por_categoria = {}
    for t in base_de_datos:
        if t.categoria in gastos_por_categoria:
            gastos_por_categoria[t.categoria] += t.cantidad
        else:
            gastos_por_categoria[t.categoria] = t.cantidad

    return {
        "total_transacciones": len(base_de_datos),
        "total_gastos": total_gastos,
        "desglose_por_categoria": gastos_por_categoria,
    }
