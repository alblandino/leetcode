# 85. Maximal Rectangle

- **Dificultad:** Dificil
- **Enlace:** https://leetcode.com/problems/maximal-rectangle/

## Problema

Se recibe una matriz de caracteres `'0'` y `'1'`. Hay que encontrar el rectangulo mas grande (alineado con las filas y columnas) que tenga solo `'1'` adentro, y devolver su area.

## Ejemplos

```
Entrada: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Salida: 6
```

El rectangulo de area 6 ocupa las columnas 2 a 4 de las filas 1 y 2.

```
Entrada: matrix = [["0"]]
Salida: 0
```

```
Entrada: matrix = [["1"]]
Salida: 1
```

## Restricciones

- `rows == matrix.length`
- `cols == matrix[i].length`
- `1 <= rows, cols <= 200`
- `matrix[i][j]` es `'0'` o `'1'`.

## Solucion

Se reduce al problema 84 (Largest Rectangle in Histogram). Se recorre la matriz fila por fila y se mantiene un arreglo `heights`: para cada columna, cuantos `'1'` seguidos hay hacia arriba terminando en la fila actual. Si la celda es `'1'` la altura sube en 1; si es `'0'` vuelve a 0.

Con eso, cada fila es la base de un histograma, y el rectangulo mas grande que termina en esa fila es el rectangulo mas grande de ese histograma. Ese calculo se hace con la pila monotona del problema 84 en O(cols). La respuesta es el maximo entre todas las filas.

Probar todos los rectangulos posibles seria O(rows^2 * cols^2) o peor.

## Complejidad

- Tiempo: O(rows * cols)
- Espacio: O(cols)
