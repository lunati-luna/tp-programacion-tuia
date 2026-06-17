import csv
from ej4 import obtenerAnios  # Traemos la función que ya arreglamos en ej4.py

# =====================================================================
# EJERCICIO 7: Clase y función para un año específico
# =====================================================================
class EstadisticasAnual:
    def __init__(self, anio: int, cantidad_casos: int = 0):
        self.anio = anio
        self.cantidad_casos = cantidad_casos
        
    def mostrar(self):
        # Este es el método que va a usar el print al final
        print(f"Año: {self.anio} | Casos procesados: {self.cantidad_casos}")


def crearEstadisticasAnualDesdeArchivo(archivo_entrada: str, anio_buscar: int) -> EstadisticasAnual:
    """
    Cuenta los casos de un año específico en el CSV y devuelve un objeto EstadisticasAnual.
    """
    contador_casos = 0
    try:
        with open(archivo_entrada, mode="r", encoding="utf-8") as f:
            lector = csv.reader(f)
            next(lector, None)  # Saltamos el encabezado
            
            for fila in lector:
                if fila and len(fila) > 0:
                    fecha = fila[0].strip()
                    # Si el año de la fecha coincide con el que buscamos, sumamos 1
                    if fecha and fecha.split("-")[0] == str(anio_buscar):
                        contador_casos += 1
    except FileNotFoundError:
        print(f"Error: El archivo '{archivo_entrada}' no existe.")

    # Devolvemos el objeto armado
    return EstadisticasAnual(anio=anio_buscar, cantidad_casos=contador_casos)


# =====================================================================
# EJERCICIO 8: Función que pide el enunciado
# =====================================================================
def crearObjetosEstadisticasAnual(archivo_entrada: str) -> list:
    """
    Toma el nombre de un archivo y devuelve una lista de objetos de la clase EstadisticasAnual.
    """
    lista_objetos_final = []

    anios_disponibles = obtenerAnios(archivo_entrada)

    for anio in anios_disponibles:
        resultado = crearEstadisticasAnualDesdeArchivo(archivo_entrada, anio)
        
        # Como ahora sabemos seguro que devuelve un objeto (y no una lista), lo agregamos directo
        lista_objetos_final.append(resultado)

    return lista_objetos_final


# =====================================================================
# INVOCACIÓN FINAL
# =====================================================================
if __name__ == "__main__":
    print("--- Procesando Estadísticas Anuales ---")
    
    objetos_estadisticas = crearObjetosEstadisticasAnual("datos_filtrados.csv")

    print(f"Se generó una lista con {len(objetos_estadisticas)} objetos EstadisticasAnual.\n")

    print("Detalle de los objetos:")
    print("-" * 40)
    for objeto in objetos_estadisticas:
        objeto.mostrar()
    print("-" * 40)