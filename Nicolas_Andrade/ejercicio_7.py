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

def validate_args(q):
    if q >= 2:
        return True
    else:
        return False

def main():
    q_args = len(sys.argv)
    validate_q = validate_args(q_args)
    if validate_q:
        print("La cantidad de argumentos es valida!")
    else:
        print("La cantidad de argumentos es invalida.")
if __name__ == "__main__":
    main()