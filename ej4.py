import csv

def obtenerAnios(archivo_entrada: str) -> list[int]:
    anios_unicos = set()  # Usamos set para evitar repetidos

    try:
        with open(archivo_entrada, mode="r", encoding="utf-8") as f_entrada:
            lector = csv.reader(f_entrada)
            next(lector, None)  # Saltamos el encabezado
            
            for fila in lector:
                if fila and len(fila) > 0:
                    # 1. Agarramos el string de la fecha de la primera columna
                    fecha = fila[0].strip()  
                    
                    if fecha:
                        # 2. Separamos por el guion. Esto nos da una LISTA: ['YYYY', 'MM', 'DD']
                        partes = fecha.split("-")
                        
                        # 3. Extraemos SOLO el primer elemento de esa lista (el año)
                        anio_str = partes[0]
                        
                        # 4. Validamos y lo guardamos convertido a NÚMERO ENTERO (int)
                        if anio_str.isdigit() and len(anio_str) == 4:
                            anios_unicos.add(int(anio_str))
                            
    except FileNotFoundError:
        print(f"Error: El archivo '{archivo_entrada}' no existe.")
        return []

    # Como ahora anios_unicos tiene SOLO números enteros, el sorted() no va a fallar
    return sorted(list(anios_unicos), reverse=True)
# --- INVOCACIÓN PARA MOSTRAR LA LISTA EN LA TERMINAL ---

lista_de_anios = obtenerAnios("datos_filtrados.csv")
print("La lista de años (de mayor a menor) es:")
print(lista_de_anios)