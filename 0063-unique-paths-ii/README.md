# 63. Unique Paths II

- **Dificultad:** Media
- **Enlace:** https://leetcode.com/problems/unique-paths-ii/

## Problema

Igual que el problema 62: un robot va de la esquina superior izquierda a la inferior derecha de una cuadricula moviendose solo a la derecha o hacia abajo. La diferencia es que ahora algunas casillas tienen obstaculos (marcadas con `1`) y el robot no puede pasar por ellas. Las casillas libres valen `0`.

Hay que contar cuantos caminos validos hay. Si la salida o la meta tienen un obstaculo, la respuesta es 0. La respuesta no pasa de `2 * 10^9`.

## Ejemplos

```
Entrada: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
Salida: 2
```

El obstaculo del centro deja solo dos caminos: rodear por arriba o por la izquierda.

```
Entrada: obstacleGrid = [[0,1],[0,0]]
Salida: 1
```

## Restricciones

- `m == obstacleGrid.length`
- `n == obstacleGrid[i].length`
- `1 <= m, n <= 100`
- `obstacleGrid[i][j]` es 0 o 1.

## Solucion

Programacion dinamica con una sola fila `dp`, igual que en el 62. Los caminos hasta una casilla son los de arriba mas los de la izquierda, salvo que la casilla tenga un obstaculo: en ese caso vale 0, porque ningun camino puede pasar por ahi.

Se empieza con `dp[0] = 1` (la salida) y se procesa fila por fila. Asi no hace falta tratar aparte la primera fila y la primera columna: un obstaculo en ellas deja en 0 todo lo que viene despues en esa linea.

## Complejidad

- Tiempo: O(m * n)
- Espacio: O(n)
