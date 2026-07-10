# Ejercicio 1: Decodificación de Huffman (Huffman Decoding)

Este ejercicio contiene la solución en Python para el problema **"Tree: Huffman Decoding"** de HackerRank.\
[Tree: Huffman Decoding](https://www.hackerrank.com/challenges/tree-huffman-decoding/problem)

## Descripción del Problema

La codificación de Huffman es un algoritmo utilizado para la compresión de datos sin pérdida. Asigna códigos de longitud variable a los caracteres de entrada, basándose en sus frecuencias. Los caracteres más frecuentes obtienen códigos más cortos, y los menos frecuentes obtienen códigos más largos.

En este problema, se proporciona la raíz de un árbol de Huffman y una cadena binaria codificada `s`. El objetivo es decodificar la cadena binaria y retornar el texto original.

### Reglas de Decodificación:
- Comenzamos desde la raíz del árbol de Huffman.
- Leemos la cadena binaria de izquierda a derecha bit por bit:
  - Si el bit es `0`, nos movemos al hijo izquierdo (`left`).
  - Si el bit es `1`, nos movemos al hijo derecho (`right`).
- Si llegamos a un nodo hoja (un nodo que no tiene hijos izquierdo ni derecho), hemos decodificado un carácter:
  - Añadimos el carácter del nodo hoja al resultado decodificado.
  - Regresamos a la raíz del árbol para decodificar el siguiente carácter utilizando el resto de la cadena binaria.

---

## Estructura del Proyecto

La estructura de la carpeta `exercise1/` es la siguiente:

```text
exercise1/
├── README.md           # Este archivo de documentación
├── main.py             # Script principal con la función de decodificación y pruebas locales
└── encode/
    └── encode.py       # Módulo auxiliar para construir el árbol de Huffman y generar las cadenas de prueba
```

## Pruebas Ejecutadas

El archivo `main.py` contiene tres casos de prueba:

1. **Test 1**: Cadena original: `ABACA`
2. **Test 2**: Cadena original: `Rumpelstiltskin`
3. **Test 3**: Cadena original: `howmuchwoodwouldawoodchuckchuckifawoodchuckcouldchuckwood?`

---

## Instrucciones de Ejecución

Para ejecutar las pruebas localmente, asegúrate de estar en el directorio raíz del proyecto y corre el siguiente comando en tu terminal:

```bash
python3 exercise1/main.py
```

### Salida Esperada:
```text
Test 1
Result: ABACA

Test 2
Result: Rumpelstiltskin

Test 3
Result: howmuchwoodwouldawoodchuckchuckifawoodchuckcouldchuckwood?
```

---

## Construcción del Árbol y Proceso de Decodificación

A continuación se detalla cómo se construye el árbol de Huffman a partir de la cadena de ejemplo `"ABACA"` y cómo funciona el proceso de decodificación paso a paso.

### Paso 1. Contar frecuencias

Supongamos que el texto original es:
**`ABACA`**

Contamos cuántas veces aparece cada letra (frecuencia):

| Letra | Frecuencia |
| :---: | :--------: |
|   A   |     3      |
|   B   |     1      |
|   C   |     1      |

### Paso 2. Crear los nodos hoja

Primero se crean los tres nodos para los caracteres individuales:
- `A(3)`
- `B(1)`
- `C(1)`

### Paso 3. Unir los dos menores

Siempre se toman las dos frecuencias más pequeñas para unirlas. En este caso son `B(1)` y `C(1)`.

```text
  B(1)
  C(1)
  A(3)
```

Al unir `B` y `C`, creamos un nuevo nodo padre cuya frecuencia es la suma de ambos (`1 + 1 = 2`):

```text
      (2)
     /   \
   B(1)  C(1)
```

### Paso 4. Volver a ordenar y unir

Ahora nos quedan los siguientes nodos por unir:
- Nodo intermedio `(2)`
- Nodo `A(3)`

Los unimos bajo una nueva raíz (root), que tendrá una frecuencia de `2 + 3 = 5` (la longitud total del texto):

```text
         (5)
        /   \
      (2)   A(3)
     /   \
   B(1) C(1)
```

Este nodo superior es el **root** de nuestro árbol de Huffman.

### Paso 5. Asignar los bits

Por convenio:
- Rama izquierda = `0`
- Rama derecha = `1`

El árbol con las etiquetas de los caminos queda así:

```text
         (root)
       0/      \1
      (2)       A
    0/   \1
   B       C
```

### Paso 6. Obtener los códigos binarios

Recorremos el árbol desde la raíz hasta cada hoja para definir los códigos:

* **Para llegar a A:**
  ```text
  root -> derecha (1) => A = 1
  ```
* **Para llegar a B:**
  ```text
  root -> izquierda (0) -> izquierda (0) => B = 00
  ```
* **Para llegar a C:**
  ```text
  root -> izquierda (0) -> derecha (1) => C = 01
  ```

### Codificando `"ABACA"`

Reemplazando cada letra por su código:
```text
A -> 1
B -> 00
A -> 1
C -> 01
A -> 1
```

La cadena codificada final es:
**`1001011`**

---

## ¿Por qué nuestra función solo recibe `root`?

El juez en línea (o nuestro script de pruebas en local) ya realiza todo el proceso de análisis de frecuencias, construcción del árbol y generación de la cadena codificada `s = "1001011"`. 

Por lo tanto, la función `decodeHuff(root, s)` solo debe encargarse de reconstruir el mensaje original leyendo `s` y recorriendo el árbol que se le entrega en `root`:

```text
             root
            (5)
           /   \
        (2)     A
       /   \
      B     C
```

### Simulación del recorrido con `s = "1001011"`:

1. **Empezamos en `root`**.
2. **Leemos `1`**: Vamos a la derecha -> Llegamos a **`A`** (hoja).
   - Guardamos **`A`** en el resultado.
   - Regresamos a `root`.
3. **Leemos `0`**: Vamos a la izquierda -> Llegamos a `(2)`.
4. **Leemos `0`**: Vamos a la izquierda -> Llegamos a **`B`** (hoja).
   - Guardamos **`B`** en el resultado.
   - Regresamos a `root`.
5. **Leemos `1`**: Vamos a la derecha -> Llegamos a **`A`** (hoja).
   - Guardamos **`A`** en el resultado.
   - Regresamos a `root`.
6. **Leemos `0`**: Vamos a la izquierda -> Llegamos a `(2)`.
7. **Leemos `1`**: Vamos a la derecha -> Llegamos a **`C`** (hoja).
   - Guardamos **`C`** en el resultado.
   - Regresamos a `root`.
8. **Leemos `1`**: Vamos a la derecha -> Llegamos a **`A`** (hoja).
   - Guardamos **`A`** en el resultado.

**Resultado decodificado:** `ABACA`

