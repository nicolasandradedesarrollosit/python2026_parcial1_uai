# Implementá una función llamada `pedir_entero()` que utilice un bucle `while True` para pedirle al usuario su edad.

# El programa debe:

# - Solicitar una edad por teclado.
# - Utilizar un bloque `try...except ValueError`.
# - Detectar si el usuario ingresa texto en lugar de un número.
# - Evitar que el programa finalice con error.
# - Volver a pedir el dato hasta que sea válido.
# - Finalizar el bucle utilizando `break` o `return`.

def pedir_entero():
    while True:
        try:
            edad = int(input("Ingrese su edad: "))
            print(f"Edad registrada: {edad}")
            return edad
        except ValueError:
            print("Debe ingresar un número válido.")

if __name__ == "__main__":
    pedir_entero()