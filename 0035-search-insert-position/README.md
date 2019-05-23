# 35. Search Insert Position

- **Dificultad:** Facil
- **Enlace:** https://leetcode.com/problems/search-insert-position/

## Problema

Se recibe un arreglo `nums` ordenado de menor a mayor, sin repetidos, y un valor `target`. Si `target` esta en el arreglo se devuelve su indice; si no esta, se devuelve el indice donde habria que meterlo para que el arreglo siga ordenado.

La solucion debe ser O(log n).

## Ejemplos

```
Entrada: nums = [1,3,5,6], target = 5
Salida: 2
```

```
Entrada: nums = [1,3,5,6], target = 2
Salida: 1
```

El 2 iria entre el 1 y el 3.

```
Entrada: nums = [1,3,5,6], target = 7
Salida: 4
```

## Restricciones

- `1 <= nums.length <= 10^4`
- `-10^4 <= nums[i] <= 10^4`
- `nums` tiene valores distintos ordenados de forma ascendente.
- `-10^4 <= target <= 10^4`

## Solucion

Es una busqueda binaria normal. Si se encuentra `target`, se devuelve `mid`. Si no, el ciclo termina cuando `left` pasa a `right`, y en ese momento `left` apunta al primer elemento mayor que `target` (o al final del arreglo si todos son menores), que es justo la posicion de insercion.

Recorrer el arreglo hasta encontrar el primer valor mayor o igual tambien sirve, pero es O(n).

## Complejidad

- Tiempo: O(log n)
- Espacio: O(1)
