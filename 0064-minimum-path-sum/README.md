# 64. Minimum Path Sum

- **Dificultad:** Media
- **Enlace:** https://leetcode.com/problems/minimum-path-sum/

## Problema

Se recibe una cuadricula de `m x n` con numeros no negativos. Hay que ir de la esquina superior izquierda a la inferior derecha moviendose solo a la derecha o hacia abajo, y encontrar el camino cuya suma de casillas (incluyendo la de salida y la de llegada) sea la menor. Se devuelve esa suma minima.

## Ejemplos

```
Entrada: grid = [[1,3,1],[1,5,1],[4,2,1]]
Salida: 7
```

El camino 1 -> 3 -> 1 -> 1 -> 1 suma 7.

```
Entrada: grid = [[1,2,3],[4,5,6]]
Salida: 12
```

## Restricciones

- `m == grid.length`
- `n == grid[i].length`
- `1 <= m, n <= 200`
- `0 <= grid[i][j] <= 200`

## Solucion

Programacion dinamica. A cada casilla se llega desde arriba o desde la izquierda, asi que el costo minimo para llegar a ella es su valor mas el menor de esos dos costos. En la primera fila solo se puede venir desde la izquierda y en la primera columna solo desde arriba.

Se usa una fila `dp` que se va actualizando fila por fila, sin modificar la cuadricula de entrada. Probar todos los caminos seria exponencial; con la tabla cada casilla se calcula una sola vez.

## Complejidad

- Tiempo: O(m * n)
- Espacio: O(n)
