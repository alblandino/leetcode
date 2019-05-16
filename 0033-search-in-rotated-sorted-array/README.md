# 33. Search in Rotated Sorted Array

- **Dificultad:** Media
- **Enlace:** https://leetcode.com/problems/search-in-rotated-sorted-array/

## Problema

Se recibe un arreglo `nums` de valores distintos que estaba ordenado de menor a mayor, pero que pudo haber sido rotado: se cortaron los primeros elementos y se pasaron al final (por ejemplo `[0,1,2,4,5,6,7]` puede llegar como `[4,5,6,7,0,1,2]`).

Hay que devolver el indice de `target` dentro de `nums`, o `-1` si no esta. La busqueda debe ser O(log n).

## Ejemplos

```
Entrada: nums = [4,5,6,7,0,1,2], target = 0
Salida: 4
```

```
Entrada: nums = [4,5,6,7,0,1,2], target = 3
Salida: -1
```

```
Entrada: nums = [1], target = 0
Salida: -1
```

## Restricciones

- `1 <= nums.length <= 5000`
- `-10^4 <= nums[i] <= 10^4`
- Todos los valores de `nums` son distintos.
- `nums` es un arreglo ascendente que posiblemente fue rotado.
- `-10^4 <= target <= 10^4`

## Solucion

Es una busqueda binaria con un paso extra. Al partir el rango en `mid`, al menos una de las dos mitades esta ordenada sin corte: si `nums[left] <= nums[mid]` es la izquierda, si no es la derecha. En la mitad ordenada se puede saber con dos comparaciones si `target` cae dentro de ella; si cae, se busca ahi, y si no, en la otra mitad.

Un recorrido lineal tambien encontraria el valor, pero seria O(n) y el problema pide O(log n).

## Complejidad

- Tiempo: O(log n)
- Espacio: O(1)
