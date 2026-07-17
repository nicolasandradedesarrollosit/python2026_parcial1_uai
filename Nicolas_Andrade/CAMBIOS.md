# Cambios de la recuperación — Nicolás Andrade

Nota original del parcial: **24/70 (3.4/10)**. Todos los ejercicios obligatorios
tenían errores conceptuales, según el informe de corrección del profesor
Alejandro Sartorio. Este documento detalla, ejercicio por ejercicio, qué estaba
mal en la entrega original y qué se corrigió.

---

## Ejercicio 1 — Variables y cadenas de texto

**Antes:** se partía el nombre con `split(" ")` y se iteraba palabra por
palabra con un `for`, capitalizando e imprimiendo cada palabra por separado
(`Tu nombre es Juan` / `Tu nombre es Perez` en líneas distintas), usando
`.capitalize()` en vez de `.title()`.

**Ahora:** una sola línea con `.strip().title()` sobre el string completo y un
único `print(f"Hola, {nombre}")`, tal como pide el enunciado (`Hola, Juan
Perez`).

**Por qué:** `.capitalize()` solo pone en mayúscula la primera letra de *todo*
el string; `.title()` la pone en la primera letra de *cada palabra*. Además no
hacía falta partir el string manualmente para lograr el resultado pedido.

---

## Ejercicio 2 — Excepciones y bucles

**Antes:** agregaba una validación de rango (edad negativa o mayor a 120) no
pedida por el enunciado, y el mensaje/formato de salida no coincidía con el
esperado.

**Ahora:** se simplifica a lo que pide el enunciado: `try/except ValueError`
sobre `int(input(...))`, mensaje `"Debe ingresar un número válido."` si falla,
y `"Edad registrada: {edad}"` al tener éxito.

**Por qué:** el ejercicio evalúa el manejo de `ValueError` ante texto inválido,
no reglas de negocio extra que no estaban pedidas y que además no estaban
contempladas en el resultado esperado del enunciado.

---

## Ejercicio 3 — Listas de comprensión

**Antes:** usaba un `for` con `range(len(...))` y `.append()` para construir la
lista.

**Ahora:** lista de comprensión en una sola línea:
`[palabra.upper() for palabra in palabras]`.

**Por qué:** el ejercicio pide explícitamente una lista de comprensión; un
bucle `for` con `.append()` no cumple la consigna aunque el resultado final
sea el mismo.

---

## Ejercicio 4 — `lambda` y `sorted()`

**Antes:** `sorted(alumnos["nombre"])` — esto falla porque `alumnos` es una
lista de diccionarios, no un diccionario; `alumnos["nombre"]` no es una
operación válida sobre una lista.

**Ahora:** `sorted(alumnos, key=lambda a: a["nombre"])` dentro de un `for`,
imprimiendo `alumno["nombre"]` de cada elemento ya ordenado.

**Por qué:** había una confusión entre indexar una lista y acceder a la clave
de un diccionario. `sorted()` necesita ordenar la lista completa usando la
clave `"nombre"` de cada diccionario como criterio, vía `key=lambda`.

---

## Ejercicio 5 — CSV con `DictReader`

**Antes:** mezclaba lógica del ejercicio 7 (validación de `sys.argv`) con el
ejercicio 5, y el `with open(file)` nunca abría un `csv.DictReader`: iteraba
directamente sobre `file` (el string con el nombre del archivo), no sobre las
filas del CSV.

**Ahora:** `ejercicio_5.py` contiene únicamente lo pedido: `with open("estudiantes.csv", ...) as archivo`, `csv.DictReader(archivo)` y un `for fila in lector: print(fila["nombre"])`.

**Por qué:** cada ejercicio se resuelve de forma aislada según su propio
enunciado; mezclar el manejo de argumentos del ejercicio 7 no tenía sentido
acá y, además, sin `csv.DictReader` nunca se accede correctamente a la columna
`"nombre"`.

---

## Ejercicio 6 — Expresiones regulares

**Antes:** no se usaba el módulo `re` (el comentario en el código decía
"olvide estudiar expresiones regulares"); la validación se hacía con
`correo.split("@")` y comparación exacta del dominio.

**Ahora:** `import re` y `re.search(r"@uai\.edu\.ar$", correo)`, con los
puntos escapados (`\.`) y el ancla de fin de línea (`$`), tal como exige el
enunciado.

**Por qué:** el ejercicio evalúa específicamente el uso de `re.search()` con
anclaje y escape de caracteres especiales; resolverlo con `split()` no
cumple la consigna, aunque el resultado pudiera parecer similar en casos
simples.

---

## Ejercicio 7 — Argumentos de línea de comandos (`sys`)

**Antes:** `validate_args` usaba `if q >= 2` (acepta 2 o más argumentos, en
vez de exigir exactamente uno) y nunca llamaba a `sys.exit()`, solo imprimía
un mensaje.

**Ahora:** `if len(sys.argv) != 2: sys.exit("Error: debe ingresar exactamente
un argumento.")`, y si es válido imprime el argumento recibido.

**Por qué:** `sys.argv[0]` es siempre el nombre del script, por lo que un solo
argumento adicional implica `len(sys.argv) == 2`. La condición original
aceptaba casos inválidos (más de un argumento) y el enunciado pedía cortar la
ejecución con `sys.exit()`, no solo avisar por consola.

---

## Ejercicio 8 — POO (`__str__`)

**Antes:** `__str__` devolvía `f"El {self.titulo} por {self.autor}"`,
agregando un prefijo "El" que no estaba en el formato pedido.

**Ahora:** `return f"{self.titulo} por {self.autor}"`, sin prefijo, igual al
resultado esperado del enunciado (`El Aleph por Jorge Luis Borges`, donde "El"
es parte del título, no una palabra agregada por el código).

**Por qué:** el prefijo hardcodeado rompía el formato para cualquier libro
cuyo título no empezara naturalmente con "El".

---

## Ejercicio 10 — Test con `pytest`

**Antes:** `calcular_cuadrado` usaba `print()` en vez de `return`, por lo que
`assert calcular_cuadrado(4) == 16` fallaba (comparaba `None` contra `16`). El
test importaba la función con una ruta absoluta de paquete
(`python2026_parcial1_uai.Nicolas_Andrade.ejercicio_10`) que no es portable.

**Ahora:** `calcular_cuadrado` hace `return n * n`, y el test importa con
`from ejercicio_10 import calcular_cuadrado` (import relativo al mismo
directorio, como espera `pytest` al ejecutarse desde la carpeta del ejercicio).

**Por qué:** una función pensada para ser testeada con `assert` debe devolver
un valor, no imprimirlo. El import absoluto además dependía de la estructura
exacta del repo del profesor y no funcionaría en otro entorno.
