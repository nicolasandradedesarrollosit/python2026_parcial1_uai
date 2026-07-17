# ## Problema 3: Programación funcional y listas de comprensión

# Dada la siguiente lista:

# ```python
# palabras = ["hola", "mundo", "python"]
# ```

# Creá una nueva lista en una sola línea utilizando una **lista de comprensión**.

# La nueva lista debe contener las mismas palabras, pero convertidas completamente a mayúsculas mediante el método `.upper()`.

def main():
    palabras = ["hola", "mundo", "python"]
    new_list = []
    for i in range (len(palabras)):
        new_list.append(palabras[i].upper())
    
    print(new_list)


if __name__ == "__main__":
    main()