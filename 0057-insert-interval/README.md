# 57. Insert Interval

- **Dificultad:** Media
- **Enlace:** https://leetcode.com/problems/insert-interval/

## Problema

Se recibe una lista de intervalos que no se cruzan entre si y que ya esta ordenada por inicio, y un intervalo nuevo `newInterval`. Hay que meter el intervalo nuevo en la lista de forma que siga ordenada y sin cruces, uniendo los intervalos que haga falta.

Dos intervalos se consideran traslapados si comparten al menos un punto. Se puede devolver una lista nueva en vez de modificar la original.

## Ejemplos

```
Entrada: intervals = [[1,3],[6,9]], newInterval = [2,5]
Salida: [[1,5],[6,9]]
```

```
Entrada: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Salida: [[1,2],[3,10],[12,16]]
```

`[4,8]` toca a `[3,5]`, `[6,7]` y `[8,10]`, y los cuatro quedan como `[3,10]`.

## Restricciones

- `0 <= intervals.length <= 10^4`
- `intervals[i].length == 2`
- `0 <= start_i <= end_i <= 10^5`
- `intervals` esta ordenado por `start_i` de forma ascendente.
- `newInterval.length == 2`
- `0 <= start <= end <= 10^5`

## Solucion

Como la lista ya esta ordenada, se recorre una sola vez en tres partes. Primero se copian los intervalos que terminan antes de que empiece el nuevo. Despues, mientras un intervalo empiece antes o justo donde termina el nuevo, se une con el (se toma el menor inicio y el mayor final). Al final se agrega el intervalo unido y se copian los que quedan.

Agregar el intervalo y volver a ordenar y unir todo tambien funciona, pero cuesta O(n log n). Aprovechar el orden lo deja en O(n).

## Complejidad

- Tiempo: O(n)
- Espacio: O(n) para la lista de salida
