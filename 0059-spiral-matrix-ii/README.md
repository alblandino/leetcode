# 59. Spiral Matrix II

- **Dificultad:** Media
- **Enlace:** https://leetcode.com/problems/spiral-matrix-ii/

## Problema

Se recibe un entero positivo `n`. Hay que construir una matriz de `n x n` y llenarla con los numeros del 1 al `n^2` siguiendo un recorrido en espiral: fila de arriba hacia la derecha, columna derecha hacia abajo, fila de abajo hacia la izquierda, columna izquierda hacia arriba, y asi hacia el centro.

## Ejemplos

```
Entrada: n = 3
Salida: [[1,2,3],[8,9,4],[7,6,5]]
```

```
Entrada: n = 1
Salida: [[1]]
```

## Restricciones

- `1 <= n <= 20`

## Solucion

Es el problema 54 al reves: en vez de leer la matriz en espiral, se escribe. Se crea una matriz de ceros y se guardan cuatro bordes (`top`, `bottom`, `left`, `right`). En cada vuelta se llenan la fila de arriba, la columna derecha, la fila de abajo y la columna izquierda con un contador que va subiendo, y despues de cada lado se mueve el borde correspondiente hacia adentro.

El ciclo termina cuando los bordes se cruzan. Como la matriz es cuadrada, cuando `n` es impar el centro queda como una vuelta de un solo elemento.

## Complejidad

- Tiempo: O(n^2)
- Espacio: O(1) extra, sin contar la matriz de salida
