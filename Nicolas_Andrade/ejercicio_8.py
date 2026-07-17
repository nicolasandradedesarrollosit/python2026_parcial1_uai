# ## Problema 8: Programación Orientada a Objetos

# > Este ejercicio debe resolverse primero en papel, sin utilizar computadora.

# Definí una clase llamada `Libro`.

# La clase debe:

# - Tener un método constructor `__init__`.
# - Recibir y asignar los atributos `titulo` y `autor`.
# - Implementar el método especial `__str__`.
# - Permitir que, al imprimir un objeto con `print()`, se muestre una cadena con el siguiente formato:

# ```text
# Título por Autor
# ```

# ### Ejemplo de uso esperado

# ```python
# libro = Libro("El Aleph", "Jorge Luis Borges")
# print(libro)
# ```

# ### Resultado esperado

# ```text
# El Aleph por Jorge Luis Borges
# ```

class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def __str__(self):
        return f"{self.titulo} por {self.autor}"

if __name__ == "__main__":
    libro = Libro("El Aleph", "Jorge Luis Borges")
    print(libro)