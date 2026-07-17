# Escribí un programa que solicite al usuario su nombre.

# El programa debe:

# - Eliminar los espacios en blanco al principio y al final del texto ingresado.
# - Convertir la primera letra de cada palabra a mayúscula.
# - Imprimir un saludo en consola utilizando cadenas formateadas `f-strings`.
def main():
    nombre = input("Ingrese su nombre: ").strip().title()
    print(f"Hola, {nombre}")

if __name__ == "__main__":
    main()