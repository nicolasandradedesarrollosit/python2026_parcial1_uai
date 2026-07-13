# ## Problema 6: Expresiones regulares

# Asumiendo que importaste la biblioteca `re`, escribí una instrucción condicional `if` que utilice la función `re.search()` para validar si una variable `correo`, ingresada por el usuario, termina estrictamente en:

# ```text
# @uai.edu.ar
# ```

# El programa debe:

# - Usar el anclaje de fin de línea `$`.
# - Escapar correctamente los puntos con `\.` para que sean interpretados como caracteres literales.
# - Mostrar un mensaje indicando si el correo es válido o inválido.

# ### Ejemplo válido

# ```text
# alumno@uai.edu.ar
# ```

# ### Ejemplo inválido

# ```text
# alumno@uai.com
# ```

# ---

import re

def main():
    correo = input("Ingresa un correo electronico: ")
    if re.search(r"@uai\.edu\.ar$", correo):
        print("El correo es valido")
    else:
        print("El correo es invalido")

if __name__ == "__main__":
    main()