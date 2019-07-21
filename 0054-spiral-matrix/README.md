# 54. Spiral Matrix

- **Dificultad:** Media
- **Enlace:** https://leetcode.com/problems/spiral-matrix/

## Problema

Se recibe una matriz de `m` filas y `n` columnas. Hay que devolver todos sus elementos en orden de espiral: primero la fila de arriba de izquierda a derecha, luego bajando por la columna derecha, despues la fila de abajo hacia la izquierda, subiendo por la columna izquierda, y asi hacia el centro.

## Ejemplos

```
Entrada: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Salida: [1,2,3,6,9,8,7,4,5]
```

```
Entrada: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Salida: [1,2,3,4,8,12,11,10,9,5,6,7]
```

## Restricciones

- `m == matrix.length`
- `n == matrix[i].length`
- `1 <= m, n <= 10`
- `-100 <= matrix[i][j] <= 100`

## Solucion

Se guardan cuatro bordes: `top`, `bottom`, `left` y `right`. En cada vuelta se recorre la fila de arriba y se baja `top`, la columna derecha y se mueve `right` a la izquierda, la fila de abajo (hacia atras) y se sube `bottom`, y la columna izquierda (hacia arriba) y se mueve `left` a la derecha.

Antes de recorrer la fila de abajo y la columna izquierda se revisa que los bordes no se hayan cruzado. Sin esa revision, una matriz de una sola fila o una sola columna repetiria elementos. Cada elemento se visita una sola vez.

## Complejidad

- Tiempo: O(m * n)
- Espacio: O(1) extra, sin contar la lista de salida
