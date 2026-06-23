def categorizar_transaccion(concepto: str) -> str:
    """
    Analiza el concepto de la transacción y devuelve una categoría sugerida.
    """
    # Convertimos el texto a minúsculas para que la búsqueda no falle por mayúsculas
    concepto_lower = concepto.lower()

    # Diccionario de reglas: { "Nombre de Categoría": ["palabras", "clave"] }
    reglas = {
        "Alimentación": ["mercadona", "carrefour", "dia", "lidl", "supermercado", "panadería"],
        "Suscripciones": ["netflix", "spotify", "hbo", "amazon", "gimnasio"],
        "Mascotas": ["veterinario", "pienso", "gala", "collar", "royal canin"],
        "Transporte": ["renfe", "uber", "cabify", "gasolinera", "repsol", "bus"],
        "Ocio": ["cine", "cena", "restaurante", "cervezas", "concierto", "hamburguesería"]
    }

    # Recorremos el diccionario para buscar coincidencias
    for categoria, palabras_clave in reglas.items():
        for palabra in palabras_clave:
            if palabra in concepto_lower:
                return categoria  # Si encuentra una palabra clave, devuelve la categoría inmediatamente

    return "Sin clasificar" # Si no encuentra nada, lo deja sin clasificar