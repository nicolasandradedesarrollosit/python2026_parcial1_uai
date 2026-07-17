# Dada la siguiente lista de diccionarios:

# ```python
# alumnos = [
#     {"nombre": "Zack", "casa": "Slytherin"},
#     {"nombre": "Ana", "casa": "Gryffindor"}
# ]
# ```

# Escribí una única línea de código que utilice:

# - Un bucle `for`.
# - La función `sorted()`.
# - Una función `lambda` en el parámetro `key`.

# El objetivo es recorrer la lista ordenada alfabéticamente tomando como referencia la clave `"nombre"` de cada diccionario.


def main():
    alumnos = [
        {"nombre": "Zack", "casa": "Slytherin"},
        {"nombre": "Ana", "casa": "Gryffindor"}
    ]

    for alumno in sorted(alumnos, key=lambda a: a["nombre"]):
        print(alumno["nombre"])

if __name__ == "__main__":
    main()