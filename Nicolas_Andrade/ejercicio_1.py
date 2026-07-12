# Escribí un programa que solicite al usuario su nombre.

# El programa debe:

# - Eliminar los espacios en blanco al principio y al final del texto ingresado.
# - Convertir la primera letra de cada palabra a mayúscula.
# - Imprimir un saludo en consola utilizando cadenas formateadas `f-strings`.
def main():
    input_str = input("Ingrese su nombre: ")
    split_input = input_str.split(" ")
    for i in range (len(split_input)):
        escape_input = split_input[i].strip().capitalize()
        print(f"Tu nombre es {escape_input}")
if __name__ == "__main__":
    main()