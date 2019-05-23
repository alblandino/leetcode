# 36. Valid Sudoku

- **Dificultad:** Media
- **Enlace:** https://leetcode.com/problems/valid-sudoku/

## Problema

Se recibe un tablero de Sudoku de 9 x 9 a medio llenar, donde `'.'` es una casilla vacia. Hay que decir si las casillas llenas respetan las reglas: ningun digito se repite en una fila, en una columna ni en ninguna de las nueve cajas de 3 x 3.

No hace falta saber si el tablero tiene solucion; solo se revisan los numeros que ya estan puestos.

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
Salida: true
```

```
Entrada: board =
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Salida: false
```

Es el mismo tablero pero con un 8 en la esquina superior izquierda, y esa caja ya tenia otro 8.

## Restricciones

- `board.length == 9`
- `board[i].length == 9`
- `board[i][j]` es un digito del 1 al 9 o `'.'`.

## Solucion

Se recorre el tablero una sola vez con un set por cada fila, uno por cada columna y uno por cada caja. La caja de la casilla `(r, c)` se numera como `(r // 3) * 3 + c // 3`, que da un valor de 0 a 8. Si un digito ya esta en el set de su fila, su columna o su caja, el tablero no es valido; si no, se agrega a los tres.

Revisar por separado cada fila, cada columna y cada caja tambien funciona, pero son tres recorridos. Con los sets se hace todo en uno.

## Complejidad

- Tiempo: O(1), porque el tablero siempre tiene 81 casillas
- Espacio: O(1), entre todos los sets se guardan como maximo 3 * 81 valores
