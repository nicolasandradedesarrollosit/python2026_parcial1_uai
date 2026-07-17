# ## Problema 7: Argumentos de línea de comandos con `sys`

# Escribí un script que verifique si el usuario introdujo exactamente un argumento adicional al ejecutar el programa desde la terminal.

# El programa debe asumir que se importó la librería `sys`.

# Si el usuario ingresa menos argumentos o más argumentos de los esperados, el programa debe salir de inmediato imprimiendo un mensaje de error utilizando `sys.exit()`.

# ### Ejemplo de ejecución válida

# ```bash
# python ejercicio_7.py archivo.txt
# ```

# ### Ejemplos de ejecución inválida

# ```bash
# python ejercicio_7.py
# python ejercicio_7.py archivo1.txt archivo2.txt
# ```

# ---

import sys

def main():
    if len(sys.argv) != 2:
        sys.exit("Error: debe ingresar exactamente un argumento.")
    print(f"Argumento recibido: {sys.argv[1]}")

if __name__ == "__main__":
    main()