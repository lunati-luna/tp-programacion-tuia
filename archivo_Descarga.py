import requests
datosVG2020 = "https://raw.githubusercontent.com/omlisandro26/datos-violencia-genero/main/linea144-2020.csv"
datosVG2021 = "https://raw.githubusercontent.com/omlisandro26/datos-violencia-genero/main/linea144-2021.csv"
datosVG2022 = "https://raw.githubusercontent.com/omlisandro26/datos-violencia-genero/main/linea144-enero-diciembre-2022.csv"

def descargarCSV(url, archivo_salida):
    print("Descargando archivo...")
    consulta = requests.get(url)
    contenido = consulta.content

    print("Guardando archivo...")
    # Abrir conexion en modo escritura
    with open(archivo_salida, "w", encoding="utf-8-sig") as archivo:
        # Escribir el contenido de la consulta
        archivo.write(contenido.decode("utf-8-sig"))

    print("¡Archivo descargado con éxito!")

descargarCSV(datosVG2020, "datosVG2020.csv")
descargarCSV(datosVG2021, "datosVG2021.csv")
descargarCSV(datosVG2022, "datosVG2022.csv")