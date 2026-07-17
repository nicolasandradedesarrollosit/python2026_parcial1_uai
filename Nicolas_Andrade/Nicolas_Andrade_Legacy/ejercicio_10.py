# ## Problema 10: Automatización de pruebas unitarias con `pytest`

# Supongamos que tenés la siguiente función en tu programa:

# ```python
# def calcular_cuadrado(n):
#     return n * n
# ```

# En un archivo de pruebas separado, escribí una función llamada:

# ```python
# test_calcular_cuadrado()
# ```

# La función debe:

# - Agrupar al menos dos validaciones.
# - Utilizar la palabra clave `assert`.
# - Verificar el resultado con un número positivo.
# - Verificar el resultado con cero.
# - Estar lista para ser ejecutada con el framework `pytest`.

# ### Ejemplo esperado

# ```python
# def test_calcular_cuadrado():
#     assert calcular_cuadrado(4) == 16
#     assert calcular_cuadrado(0) == 0
# ```

# ---

def calcular_cuadrado(numero = 1):
    print(numero * numero)

calcular_cuadrado()