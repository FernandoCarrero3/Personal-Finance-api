from fastapi import APIRouter
from app.models import Transaccion

# 1. Inicializamos el Router (le ponemos un prefijo para no repetir "/transacciones" todo el rato)
router = APIRouter(prefix="/transacciones", tags=["Transacciones"])

# Traemos nuestra base de datos simulada aquí
base_de_datos = []

# 2. Las rutas ahora usan @router en lugar de @app
# Fíjate que la ruta es "/" porque el prefijo ya añade "/transacciones"
@router.get("/")
def obtener_transacciones():
    return base_de_datos

@router.post("/")
def registrar_transaccion(transaccion: Transaccion):
    base_de_datos.append(transaccion)
    return {
        "mensaje": "Transacción registrada con éxito",
        "transaccion": transaccion
    }

# 3. La ruta de analíticas (quedará como /transacciones/analiticas)
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