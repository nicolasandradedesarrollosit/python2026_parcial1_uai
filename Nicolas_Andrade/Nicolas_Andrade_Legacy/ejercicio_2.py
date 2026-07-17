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
            edad = input("Ingrese la edad por teclado: ")
            escape_edad = int(edad)
            if escape_edad < 0 or escape_edad > 120:
                raise ValueError("La edad es mayor a 120 o negativa")
            print(f"La edad es {escape_edad}")
            break
        except ValueError as e:
            print(e)

pedir_entero()