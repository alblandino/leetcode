# 52. N-Queens II

- **Dificultad:** Dificil
- **Enlace:** https://leetcode.com/problems/n-queens-ii/

## Problema

Es el mismo problema de las `n` reinas: poner `n` reinas en un tablero de `n x n` sin que ninguna ataque a otra (ni misma fila, ni misma columna, ni misma diagonal).

La diferencia es que ahora no hay que devolver los tableros, solo cuantas soluciones distintas existen.

## Ejemplos

```
Entrada: n = 4
Salida: 2
```

```
Entrada: n = 1
Salida: 1
```

## Restricciones

- `1 <= n <= 9`

## Solucion

Backtracking fila por fila, igual que en el problema 51. En cada fila se prueba cada columna y se avanza solo si la casilla no esta atacada. Cada vez que se logra llenar la ultima fila se cuenta una solucion.

Para revisar ataques en O(1) se guardan tres conjuntos: columnas usadas, diagonales (`row - col`) y antidiagonales (`row + col`). Como no hace falta armar tableros, la funcion recursiva solo devuelve cuantas soluciones hay desde la fila actual.

## Complejidad

- Tiempo: O(n!)
- Espacio: O(n) para la recursion y los conjuntos
