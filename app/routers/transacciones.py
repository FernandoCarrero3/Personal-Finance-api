from fastapi import APIRouter
from app.models import Transaccion
from app.utils import categorizar_transaccion
from app.database import cargar_transacciones, guardar_transacciones # Nuevas importaciones

router = APIRouter(prefix="/transacciones", tags=["Transacciones"])

# ¡Hemos eliminado la variable base_de_datos = []!

@router.get("/")
def obtener_transacciones():
    return cargar_transacciones() # Leemos directamente del archivo

@router.post("/")
def registrar_transaccion(transaccion: Transaccion):
    if transaccion.categoria == "Sin clasificar":
        transaccion.categoria = categorizar_transaccion(transaccion.concepto)
        
    # 1. Cargamos los datos actuales
    datos = cargar_transacciones()
    # 2. Añadimos el nuevo dato
    datos.append(transaccion)
    # 3. Guardamos todo de vuelta en el archivo
    guardar_transacciones(datos)
    
    return {
        "mensaje": "Transacción registrada con éxito",
        "transaccion": transaccion
    }

@router.get("/analiticas")
def obtener_analiticas():
    datos = cargar_transacciones() # Leemos del archivo
    
    total_gastos = sum(t.cantidad for t in datos)
    
    gastos_por_categoria = {}
    for t in datos:
        if t.categoria in gastos_por_categoria:
            gastos_por_categoria[t.categoria] += t.cantidad
        else:
            gastos_por_categoria[t.categoria] = t.cantidad
            
    return {
        "total_transacciones": len(datos),
        "total_gastos": total_gastos,
        "desglose_por_categoria": gastos_por_categoria
    }