# 48. Rotate Image

- **Dificultad:** Media
- **Enlace:** https://leetcode.com/problems/rotate-image/

## Problema

Se recibe una matriz cuadrada de `n x n` que representa una imagen. Hay que girarla 90 grados en el sentido de las manecillas del reloj.

El giro se hace sobre la misma matriz: no se puede crear otra matriz para copiar el resultado.

## Ejemplos

```
Entrada: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Salida: [[7,4,1],[8,5,2],[9,6,3]]
```

```
Entrada: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Salida: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
```

## Restricciones

- `n == matrix.length == matrix[i].length`
- `1 <= n <= 20`
- `-1000 <= matrix[i][j] <= 1000`

## Solucion

Girar 90 grados a la derecha es lo mismo que hacer dos pasos sencillos. Primero se transpone la matriz: se intercambia `matrix[i][j]` con `matrix[j][i]` para todo `j > i`, lo que convierte filas en columnas. Despues se invierte cada fila. Revisando una posicion: el valor de `(i, j)` termina en `(j, n - 1 - i)`, que es justo donde lo deja el giro.

Copiar a una matriz nueva con `nueva[j][n - 1 - i] = matrix[i][j]` es mas directo, pero usa O(n^2) de memoria extra y el problema lo prohibe.

## Complejidad

- Tiempo: O(n^2)
- Espacio: O(1)
