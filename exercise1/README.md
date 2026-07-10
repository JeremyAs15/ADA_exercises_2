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
