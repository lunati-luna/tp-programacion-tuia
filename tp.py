import csv


def fusionarArchivosCSV(lista_archivos_entrada: list[str], archivo_salida: str) -> None:
  """
  fusionarArchivosCSV recibe una lista con los nombres de los archivos a fusionar archivo (con el formato
  publicado de la linea 144) y genera un nuevo archivo en memoria con todos los contenidos de los archivos
  recien mencionados. No devuelve nada.
  """
  filas_finales = []
  columnas = None

  for nombre_archivo in lista_archivos_entrada:
    with open(nombre_archivo, encoding="utf-8-sig") as f:
      # los archivos originales traen un \r de mas en cada linea (quedan
      # terminadas en "\r\r\n"), por eso se normaliza antes de leer con csv
      texto = f.read().replace("\r\n", "\n").replace("\r", "\n")

    lector = csv.DictReader(texto.splitlines())
    if columnas is None:
      columnas = lector.fieldnames

    for fila in lector:
      # en datosVG2022.csv la columna se llama "Fecha" en vez de "fecha"
      fecha = fila.get("fecha") or fila.pop("Fecha", None)
      provincia = fila["prov_residencia_persona_en_situacion_violencia"]
      if fecha and provincia:
        fila["fecha"] = fecha
        fila.pop("", None)  # descarta columna fantasma vacia (datosVG2022.csv)
        filas_finales.append(fila)

  with open(archivo_salida, "w", newline="", encoding="utf-8-sig") as f:
    escritor = csv.DictWriter(f, fieldnames=columnas)
    escritor.writeheader()
    escritor.writerows(filas_finales)


help(fusionarArchivosCSV)

# invocar la función
fusionarArchivosCSV(["datosVG2020.csv", "datosVG2021.csv", "datosVG2022.csv"], "datos_filtrados.csv")