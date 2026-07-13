# ## Problema 5: Manejo de archivos y librería CSV

# Escribí un fragmento de código que utilice el gestor de contexto `with open(...)` para abrir un archivo existente llamado `estudiantes.csv` en modo lectura.

# El programa debe:

# - Importar la librería `csv`.
# - Utilizar `csv.DictReader`.
# - Iterar sobre las filas del archivo.
# - Imprimir el valor de la columna `"nombre"` de cada registro.

# ### Ejemplo de archivo `estudiantes.csv`

import csv

def main():
    with open("estudiantes.csv", "r", encoding="UTF-8") as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            print(fila["nombre"])

if __name__ == "__main__":
    main()