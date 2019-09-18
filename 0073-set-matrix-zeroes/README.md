# 73. Set Matrix Zeroes

- **Dificultad:** Media
- **Enlace:** https://leetcode.com/problems/set-matrix-zeroes/

## Problema

Se recibe una matriz de enteros de `m x n`. Por cada celda que valga 0 en la matriz original, toda su fila y toda su columna deben quedar en 0.

El cambio se hace directamente sobre la matriz recibida; el metodo no devuelve nada.

## Ejemplos

```
Entrada: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Salida: [[1,0,1],[0,0,0],[1,0,1]]
```

```
Entrada: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Salida: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
```

Los ceros de la primera fila apagan esa fila y las columnas 0 y 3.

## Restricciones

- `m == matrix.length`
- `n == matrix[0].length`
- `1 <= m, n <= 200`
- `-2^31 <= matrix[i][j] <= 2^31 - 1`

## Solucion

El problema es no confundir los ceros originales con los que se van poniendo. Lo directo es copiar la matriz (O(m * n) de espacio) o guardar en dos conjuntos que filas y columnas tienen un cero (O(m + n)). Para usar espacio constante, la propia primera fila y la primera columna sirven de marcas.

Primero se anota en dos variables si la primera fila y la primera columna tenian algun cero. Despues, por cada cero en el resto de la matriz, se pone en 0 el inicio de su fila (`matrix[r][0]`) y de su columna (`matrix[0][c]`). Luego se recorren las celdas que no estan en la primera fila ni columna y se ponen en 0 si su fila o su columna esta marcada. Al final se limpian la primera fila y la primera columna si las variables lo indican. Se dejan para el final porque si se tocaran antes borrarian las marcas.

## Complejidad

- Tiempo: O(m * n)
- Espacio: O(1)
