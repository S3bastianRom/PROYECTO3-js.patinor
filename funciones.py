#Punto 1 | ¿Esto es Sano?
def esto_es_sano(calorias, es_vegetariano)->bool:
    if calorias < 100 or es_vegetariano:
        return True
    else:
        raise ValueError  (False)
    

#Punto 2 | Las Calorías
def las_calorías(ingredientes) -> float:
    total_kcal = round(sum(ingrediente.calorias for ingrediente in ingredientes), 2)
    return total_kcal


#Punto 3 | Costos
def costos (producto) -> float:
    total_costo = sum(i.ingrediente.precio for i in producto.producto_ingredientes)
    return total_costo


#Punto 4 | Rentabilidad
def rentabilidad(producto)->float:
    total_cost = costos (producto)
    calculo_rentable = (producto.precio - total_cost)

    return calculo_rentable

#Punto 5 | El mejor producto
def mejor_producto(*productos)->str:
    if not productos:
        raise ValueError ("No hay productos disponibles")

    return max(productos, key=rentabilidad).nombre
