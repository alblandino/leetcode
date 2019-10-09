# 79. Word Search

- **Dificultad:** Media
- **Enlace:** https://leetcode.com/problems/word-search/

## Problema

Se tiene una cuadricula de letras `board` y una palabra `word`. Hay que decir si la palabra se puede escribir recorriendo celdas vecinas de la cuadricula, una letra por celda.

Solo valen los movimientos arriba, abajo, izquierda y derecha (no en diagonal), y una misma celda no se puede usar dos veces dentro de la palabra.

## Ejemplos

```
Entrada: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Salida: true
```

```
Entrada: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Salida: true
```

```
Entrada: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Salida: false
```

Para la ultima `B` habria que volver a la celda de la primera `B`, y eso no se permite.

## Restricciones

- `m == board.length`
- `n = board[i].length`
- `1 <= m, n <= 6`
- `1 <= word.length <= 15`
- `board` y `word` solo tienen letras del alfabeto ingles, minusculas y mayusculas.

## Solucion

Se prueba cada celda como punto de partida y desde ahi se hace una busqueda en profundidad (DFS) con backtracking. En cada paso se revisa que la celda este dentro de la cuadricula y que tenga la letra que toca; si es asi, se marca como usada (se cambia temporalmente por `#`) y se sigue con las cuatro vecinas buscando la siguiente letra. Al volver se restaura la letra original para que otros caminos la puedan usar.

Antes de buscar se hace una poda barata: se cuentan las letras del tablero y de la palabra. Si a la cuadricula le faltan letras para formar la palabra, se responde `false` sin explorar nada.

## Complejidad

- Tiempo: O(m * n * 3^L), donde L es el largo de la palabra (desde cada celda se abren a lo sumo 3 caminos nuevos por paso)
- Espacio: O(L) por la profundidad de la recursion
