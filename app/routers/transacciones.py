from fastapi import APIRouter
from app.models import Transaccion
from app.utils import categorizar_transaccion  # 1. Importamos la función

router = APIRouter(prefix="/transacciones", tags=["Transacciones"])

base_de_datos = []

@router.get("/")
def obtener_transacciones():
    return base_de_datos

@router.post("/")
def registrar_transaccion(transaccion: Transaccion):
    # 2. Si el usuario no envió una categoría, usamos nuestro algoritmo para adivinarla
    if transaccion.categoria == "Sin clasificar":
        transaccion.categoria = categorizar_transaccion(transaccion.concepto)
        
    base_de_datos.append(transaccion)
    return {
        "mensaje": "Transacción registrada con éxito",
        "transaccion": transaccion
    }

@router.get("/analiticas")
def obtener_analiticas():
    total_gastos = sum(t.cantidad for t in base_de_datos)
    
    gastos_por_categoria = {}
    for t in base_de_datos:
        if t.categoria in gastos_por_categoria:
            gastos_por_categoria[t.categoria] += t.cantidad
        else:
            gastos_por_categoria[t.categoria] = t.cantidad
            
    return {
        "total_transacciones": len(base_de_datos),
        "total_gastos": total_gastos,
        "desglose_por_categoria": gastos_por_categoria
    }