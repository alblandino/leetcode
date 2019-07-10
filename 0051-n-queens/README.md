# 51. N-Queens

- **Dificultad:** Dificil
- **Enlace:** https://leetcode.com/problems/n-queens/

## Problema

Hay un tablero de ajedrez de `n x n` y hay que colocar `n` reinas de forma que ninguna pueda atacar a otra: dos reinas no pueden compartir fila, columna ni diagonal.

Se deben devolver todas las formas distintas de lograrlo. Cada solucion es una lista de `n` cadenas, una por fila, donde `'Q'` es una reina y `'.'` una casilla vacia. Las soluciones se pueden devolver en cualquier orden.

## Ejemplos

```
Entrada: n = 4
Salida: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
```

Con 4 reinas solo hay dos tableros validos.

```
Entrada: n = 1
Salida: [["Q"]]
```

## Restricciones

- `1 <= n <= 9`

## Solucion

Backtracking fila por fila. Como cada fila lleva exactamente una reina, en la fila actual se prueba cada columna y solo se pasa a la siguiente fila si esa casilla no esta atacada. Al llegar a la fila `n` el tablero esta completo y se guarda. Despues se quita la reina y se prueba la siguiente columna.

Para saber en O(1) si una casilla esta atacada se usan tres conjuntos: columnas ocupadas, diagonales (`row - col`) y antidiagonales (`row + col`), porque todas las casillas de una misma diagonal comparten ese valor. Probar todas las formas de poner `n` reinas en `n^2` casillas seria inviable; cortar la rama apenas hay un choque reduce mucho la busqueda.

## Complejidad

- Tiempo: O(n!), porque cada fila tiene menos columnas libres que la anterior (mas O(n^2) para armar cada tablero encontrado)
- Espacio: O(n) para la recursion y los conjuntos, sin contar la salida
