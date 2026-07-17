# Examen Práctico de Python – Nivel Integrador

**Tiempo estimado:** 60 minutos  
**Modalidad:** resolución individual  
**Repositorio de entrega:** https://github.com/cursos-uai/python2026_parcial1_uai

---

## Instrucciones generales

1. El ejercicio de **Programación Orientada a Objetos (POO)** debe resolverse primero **en papel**, sin utilizar computadora.

2. Luego de entregar el ejercicio en papel, deberán resolver todos los ejercicios en máquina, **sin ayuda de herramientas de inteligencia artificial**.

3. La resolución debe subirse al siguiente repositorio:

   https://github.com/cursos-uai/python2026_parcial1_uai

   Para realizar la entrega, cada alumno debe crear un directorio con su **nombre y apellido**, utilizando guion bajo entre ambos.

   Ejemplo:

   ```text
   Juan_Perez
   ```

4. Cada ejercicio debe estar en un archivo diferente, con el siguiente formato de nombre:

   ```text
   ejercicio_x.py
   ```

   Donde `x` representa el número de ejercicio.

   Ejemplo:

   ```text
   ejercicio_1.py
   ejercicio_2.py
   ejercicio_3.py
   ```

5. Para entregar el examen, deberán realizar un **fork** del repositorio original y luego enviar un **Pull Request** con la resolución.

---

## Criterios generales de resolución

Escribí el código necesario para resolver cada uno de los siguientes problemas. No es necesario escribir programas extensos; el objetivo es resolver el requerimiento específico de cada punto de forma clara, correcta y aplicando buenas prácticas de programación en Python.

Se valorará especialmente:

- Claridad del código.
- Uso correcto de variables, funciones, estructuras de control y librerías.
- Manejo adecuado de errores.
- Código simple, legible y mantenible.
- Cumplimiento del nombre de archivos solicitado.

---

# Problemas

---

## Problema 1: Variables y cadenas de texto

Escribí un programa que solicite al usuario su nombre.

El programa debe:

- Eliminar los espacios en blanco al principio y al final del texto ingresado.
- Convertir la primera letra de cada palabra a mayúscula.
- Imprimir un saludo en consola utilizando cadenas formateadas `f-strings`.

### Ejemplo esperado

```text
Ingrese su nombre:   juan perez
Hola, Juan Perez
```

---

## Problema 2: Excepciones y bucles

Implementá una función llamada `pedir_entero()` que utilice un bucle `while True` para pedirle al usuario su edad.

El programa debe:

- Solicitar una edad por teclado.
- Utilizar un bloque `try...except ValueError`.
- Detectar si el usuario ingresa texto en lugar de un número.
- Evitar que el programa finalice con error.
- Volver a pedir el dato hasta que sea válido.
- Finalizar el bucle utilizando `break` o `return`.

### Ejemplo esperado

```text
Ingrese su edad: veinte
Debe ingresar un número válido.
Ingrese su edad: 20
Edad registrada: 20
```

---

## Problema 3: Programación funcional y listas de comprensión

Dada la siguiente lista:

```python
palabras = ["hola", "mundo", "python"]
```

Creá una nueva lista en una sola línea utilizando una **lista de comprensión**.

La nueva lista debe contener las mismas palabras, pero convertidas completamente a mayúsculas mediante el método `.upper()`.

### Resultado esperado

```python
["HOLA", "MUNDO", "PYTHON"]
```

---

## Problema 4: Funciones anónimas y ordenación con `lambda`

Dada la siguiente lista de diccionarios:

```python
alumnos = [
    {"nombre": "Zack", "casa": "Slytherin"},
    {"nombre": "Ana", "casa": "Gryffindor"}
]
```

Escribí una única línea de código que utilice:

- Un bucle `for`.
- La función `sorted()`.
- Una función `lambda` en el parámetro `key`.

El objetivo es recorrer la lista ordenada alfabéticamente tomando como referencia la clave `"nombre"` de cada diccionario.

### Resultado esperado

```text
Ana
Zack
```

---

## Problema 5: Manejo de archivos y librería CSV

Escribí un fragmento de código que utilice el gestor de contexto `with open(...)` para abrir un archivo existente llamado `estudiantes.csv` en modo lectura.

El programa debe:

- Importar la librería `csv`.
- Utilizar `csv.DictReader`.
- Iterar sobre las filas del archivo.
- Imprimir el valor de la columna `"nombre"` de cada registro.

### Ejemplo de archivo `estudiantes.csv`

```csv
nombre,casa
Ana,Gryffindor
Zack,Slytherin
```

### Resultado esperado

```text
Ana
Zack
```

---

## Problema 6: Expresiones regulares

Asumiendo que importaste la biblioteca `re`, escribí una instrucción condicional `if` que utilice la función `re.search()` para validar si una variable `correo`, ingresada por el usuario, termina estrictamente en:

```text
@uai.edu.ar
```

El programa debe:

- Usar el anclaje de fin de línea `$`.
- Escapar correctamente los puntos con `\.` para que sean interpretados como caracteres literales.
- Mostrar un mensaje indicando si el correo es válido o inválido.

### Ejemplo válido

```text
alumno@uai.edu.ar
```

### Ejemplo inválido

```text
alumno@uai.com
```

---

## Problema 7: Argumentos de línea de comandos con `sys`

Escribí un script que verifique si el usuario introdujo exactamente un argumento adicional al ejecutar el programa desde la terminal.

El programa debe asumir que se importó la librería `sys`.

Si el usuario ingresa menos argumentos o más argumentos de los esperados, el programa debe salir de inmediato imprimiendo un mensaje de error utilizando `sys.exit()`.

### Ejemplo de ejecución válida

```bash
python ejercicio_7.py archivo.txt
```

### Ejemplos de ejecución inválida

```bash
python ejercicio_7.py
python ejercicio_7.py archivo1.txt archivo2.txt
```

---

## Problema 8: Programación Orientada a Objetos

> Este ejercicio debe resolverse primero en papel, sin utilizar computadora.

Definí una clase llamada `Libro`.

La clase debe:

- Tener un método constructor `__init__`.
- Recibir y asignar los atributos `titulo` y `autor`.
- Implementar el método especial `__str__`.
- Permitir que, al imprimir un objeto con `print()`, se muestre una cadena con el siguiente formato:

```text
Título por Autor
```

### Ejemplo de uso esperado

```python
libro = Libro("El Aleph", "Jorge Luis Borges")
print(libro)
```

### Resultado esperado

```text
El Aleph por Jorge Luis Borges
```

---

## Problema 9: POO, encapsulamiento y validaciones defensivas

Modificá la clase `Libro` del ejercicio anterior para proteger el atributo `titulo`.

El programa debe:

- Declarar el atributo como `_titulo`.
- Crear un método getter utilizando el decorador `@property`.
- Crear un método setter utilizando el decorador `@titulo.setter`.
- Validar que el título no sea vacío ni nulo.
- Levantar el siguiente error si se intenta asignar un título inválido:

```python
raise ValueError("El título no puede estar vacío")
```

### Ejemplo de uso esperado

```python
libro = Libro("Rayuela", "Julio Cortázar")
print(libro.titulo)

libro.titulo = ""
```

### Resultado esperado

```text
Rayuela
ValueError: El título no puede estar vacío
```

---

## Problema 10: Automatización de pruebas unitarias con `pytest`

Supongamos que tenés la siguiente función en tu programa:

```python
def calcular_cuadrado(n):
    return n * n
```

En un archivo de pruebas separado, escribí una función llamada:

```python
test_calcular_cuadrado()
```

La función debe:

- Agrupar al menos dos validaciones.
- Utilizar la palabra clave `assert`.
- Verificar el resultado con un número positivo.
- Verificar el resultado con cero.
- Estar lista para ser ejecutada con el framework `pytest`.

### Ejemplo esperado

```python
def test_calcular_cuadrado():
    assert calcular_cuadrado(4) == 16
    assert calcular_cuadrado(0) == 0
```

---

## Entrega final

La estructura final del repositorio debe respetar el siguiente formato:

```text
python2026_parcial1_uai/
└── Nombre_Apellido/
    ├── ejercicio_1.py
    ├── ejercicio_2.py
    ├── ejercicio_3.py
    ├── ejercicio_4.py
    ├── ejercicio_5.py
    ├── ejercicio_6.py
    ├── ejercicio_7.py
    ├── ejercicio_8.py
    ├── ejercicio_9.py
    └── ejercicio_10.py
```

Una vez finalizada la resolución, el alumno debe enviar un **Pull Request** desde su fork hacia el repositorio original.