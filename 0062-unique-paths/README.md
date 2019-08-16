# 62. Unique Paths

- **Dificultad:** Media
- **Enlace:** https://leetcode.com/problems/unique-paths/

## Problema

Un robot esta en la esquina superior izquierda de una cuadricula de `m` filas y `n` columnas y quiere llegar a la esquina inferior derecha. En cada paso solo puede moverse una casilla hacia la derecha o una hacia abajo.

Hay que contar cuantos caminos distintos llevan al robot hasta la meta. Los casos de prueba garantizan que la respuesta no pasa de `2 * 10^9`.

## Ejemplos

```
Entrada: m = 3, n = 7
Salida: 28
```

```
Entrada: m = 3, n = 2
Salida: 3
```

Los tres caminos son: derecha-abajo-abajo, abajo-abajo-derecha y abajo-derecha-abajo.

## Restricciones

- `1 <= m, n <= 100`

## Solucion

Programacion dinamica. A una casilla solo se llega desde la de arriba o desde la de la izquierda, asi que el numero de caminos hasta ella es la suma de los caminos hasta esas dos. La primera fila y la primera columna valen 1, porque solo hay una forma de recorrerlas.

No hace falta guardar toda la tabla: basta una fila `dp` donde `dp[col]` tiene los caminos de la fila anterior y se actualiza con `dp[col] += dp[col - 1]`. Probar todos los caminos con recursion simple seria exponencial.

## Complejidad

- Tiempo: O(m * n)
- Espacio: O(n)
