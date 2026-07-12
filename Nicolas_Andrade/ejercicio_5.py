# ## Problema 5: Manejo de archivos y librería CSV

# Escribí un fragmento de código que utilice el gestor de contexto `with open(...)` para abrir un archivo existente llamado `estudiantes.csv` en modo lectura.

# El programa debe:

# - Importar la librería `csv`.
# - Utilizar `csv.DictReader`.
# - Iterar sobre las filas del archivo.
# - Imprimir el valor de la columna `"nombre"` de cada registro.

# ### Ejemplo de archivo `estudiantes.csv`

import csv

import sys

def main():
    q_args = len(sys.argv)
    if q_args > 2:
        ValueError("Too many arguments...")
    if q_args < 2:
        ValueError("Too few arguments...")
    file = sys.argv[1]
    
    with open(file, "r", encoding="UTF-8"):
        for filas in file:
            print(filas["nombre"])

if __name__ == "__main__":
    main()