# 56. Merge Intervals

- **Dificultad:** Media
- **Enlace:** https://leetcode.com/problems/merge-intervals/

## Problema

Se recibe una lista de intervalos `[inicio, fin]`, sin un orden particular. Hay que unir todos los que se traslapan y devolver la lista de intervalos resultante, donde ninguno se cruza con otro y entre todos cubren lo mismo que la entrada.

Dos intervalos que solo se tocan en un extremo, como `[1,4]` y `[4,5]`, tambien cuentan como traslapados.

## Ejemplos

```
Entrada: intervals = [[1,3],[2,6],[8,10],[15,18]]
Salida: [[1,6],[8,10],[15,18]]
```

`[1,3]` y `[2,6]` se cruzan y quedan como `[1,6]`.

```
Entrada: intervals = [[1,4],[4,5]]
Salida: [[1,5]]
```

```
Entrada: intervals = [[4,7],[1,4]]
Salida: [[1,7]]
```

## Restricciones

- `1 <= intervals.length <= 10^4`
- `intervals[i].length == 2`
- `0 <= start_i <= end_i <= 10^4`

## Solucion

Primero se ordenan los intervalos por su inicio. Asi, los que se traslapan quedan juntos. Luego se recorren en orden: si el intervalo actual empieza antes o justo donde termina el ultimo intervalo unido, se extiende el final de ese ultimo con el mayor de los dos finales. Si no, empieza un intervalo nuevo.

Comparar cada intervalo contra todos los demas seria O(n^2). Despues de ordenar basta un solo recorrido.

## Complejidad

- Tiempo: O(n log n) por el ordenamiento
- Espacio: O(n) para la lista ordenada y el resultado
