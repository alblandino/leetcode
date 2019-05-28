# 37. Sudoku Solver

- **Dificultad:** Dificil
- **Enlace:** https://leetcode.com/problems/sudoku-solver/

## Problema

Se recibe un tablero de Sudoku de 9 x 9 con casillas vacias marcadas con `'.'`. Hay que llenarlas para que cada fila, cada columna y cada caja de 3 x 3 tenga los digitos del 1 al 9 sin repetir.

El tablero se modifica directamente, la funcion no devuelve nada. Siempre hay exactamente una solucion.

## Ejemplos

```
Entrada: board =
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Salida:
[["5","3","4","6","7","8","9","1","2"]
,["6","7","2","1","9","5","3","4","8"]
,["1","9","8","3","4","2","5","6","7"]
,["8","5","9","7","6","1","4","2","3"]
,["4","2","6","8","5","3","7","9","1"]
,["7","1","3","9","2","4","8","5","6"]
,["9","6","1","5","3","7","2","8","4"]
,["2","8","7","4","1","9","6","3","5"]
,["3","4","5","2","8","6","1","7","9"]]
```

## Restricciones

- `board.length == 9`
- `board[i].length == 9`
- `board[i][j]` es un digito o `'.'`.
- Se garantiza que el tablero de entrada tiene una sola solucion.

## Solucion

Se usa backtracking. Primero se recorre el tablero para guardar en sets que digitos ya hay en cada fila, columna y caja, y para hacer una lista de las casillas vacias. Luego una funcion recursiva va llenando esas casillas en orden: prueba cada digito del 1 al 9 que no este en los sets de la casilla, lo pone, marca los sets y sigue con la siguiente. Si mas adelante ninguna opcion funciona, deshace el cambio y prueba el siguiente digito.

Los sets permiten saber en O(1) si un digito se puede poner, en vez de revisar la fila, la columna y la caja completas en cada intento.

## Complejidad

- Tiempo: O(9^m) en el peor caso, donde m es la cantidad de casillas vacias (en la practica las reglas cortan casi todas las ramas)
- Espacio: O(m) por la lista de casillas vacias y la profundidad de la recursion
