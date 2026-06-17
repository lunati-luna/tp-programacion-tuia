import csv

def obtenerAnios(archivo_entrada: str) -> list[int]:
    """
    Recibe el nombre de un archivo (con el formato publicado de la línea 144)
    y devuelve la lista de años que aparecen en el archivo, ordenada de mayor a menor
    y sin elementos repetidos.
    """
    anios_unicos = set()  # Conjunto para evitar que los años se repitan

    try:
        with open(archivo_entrada, mode="r", encoding="utf-8") as f_entrada:
            lector = csv.reader(f_entrada)
            
            # Saltamos la fila de encabezados ('fecha', 'provincia', etc.)
            next(lector, None)
            
            for fila in lector:
                # Verificamos que la fila no esté vacía y tenga elementos
                if fila and len(fila) > 0:
                    fecha = fila[0].strip()  # La fecha está en la primera columna (índice 0)
                    
                    if fecha:
                        # Cortamos el string por el guion (ej: "2022-05-14" -> ["2022", "05", "14"])
                        partes = fecha.split("-")
                        anio_str = partes[0]
                        
                        # Validamos que sea un año numérico correcto de 4 dígitos
                        if anio_str.isdigit() and len(anio_str) == 4:
                            anios_unicos.add(int(anio_str))
                            
    except FileNotFoundError:
        print(f"Error: El archivo '{archivo_entrada}' no fue encontrado.")
        return []

    # Convertimos a lista y ordenamos de MAYOR a MENOR usando reverse=True
    lista_ordenada = sorted(list(anios_unicos), reverse=True)
    return lista_ordenada

# --- INVOCACIÓN PARA MOSTRAR LA LISTA EN LA TERMINAL ---

lista_de_anios = obtenerAnios("datos_filtrados.csv")
print("La lista de años (de mayor a menor) es:")
print(lista_de_anios)