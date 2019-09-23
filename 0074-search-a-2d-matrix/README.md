# 74. Search a 2D Matrix

- **Dificultad:** Media
- **Enlace:** https://leetcode.com/problems/search-a-2d-matrix/

## Problema

Se recibe una matriz de `m x n` donde cada fila esta ordenada de menor a mayor y el primer numero de cada fila es mayor que el ultimo de la fila anterior. Hay que decir si un numero `target` esta en la matriz.

La solucion debe tomar O(log(m * n)).

## Ejemplos

```
Entrada: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Salida: true
```

```
Entrada: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Salida: false
```

## Restricciones

- `m == matrix.length`
- `n == matrix[i].length`
- `1 <= m, n <= 100`
- `-10^4 <= matrix[i][j], target <= 10^4`

## Solucion

Por las dos reglas de orden, si se leen las filas una tras otra se obtiene una sola lista ordenada de `m * n` elementos. No hace falta armar esa lista: la posicion `k` de la lista corresponde a la celda `matrix[k // n][k % n]`.

Con eso se hace una busqueda binaria normal entre las posiciones `0` y `m * n - 1`. Recorrer toda la matriz seria O(m * n) y no cumple lo que pide el problema.

## Complejidad

- Tiempo: O(log(m * n))
- Espacio: O(1)
