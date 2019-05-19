# 34. Find First and Last Position of Element in Sorted Array

- **Dificultad:** Media
- **Enlace:** https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

## Problema

Se recibe un arreglo `nums` ordenado de menor a mayor (con posibles repetidos) y un valor `target`. Hay que devolver el primer y el ultimo indice donde aparece `target`.

Si `target` no esta, se devuelve `[-1, -1]`. La solucion debe ser O(log n).

## Ejemplos

```
Entrada: nums = [5,7,7,8,8,10], target = 8
Salida: [3,4]
```

```
Entrada: nums = [5,7,7,8,8,10], target = 6
Salida: [-1,-1]
```

```
Entrada: nums = [], target = 0
Salida: [-1,-1]
```

## Restricciones

- `0 <= nums.length <= 10^5`
- `-10^9 <= nums[i] <= 10^9`
- `nums` es un arreglo no decreciente.
- `-10^9 <= target <= 10^9`

## Solucion

Se hacen dos busquedas binarias con la misma funcion auxiliar. Cuando se encuentra `target` en `mid`, en vez de terminar se guarda `mid` y se sigue buscando: hacia la izquierda si se quiere la primera aparicion, o hacia la derecha si se quiere la ultima. Al cerrarse el rango, lo ultimo que se guardo es el borde buscado.

Encontrar una aparicion y luego caminar hacia los lados funciona, pero si todo el arreglo es `target` se vuelve O(n). Con dos busquedas binarias siempre es O(log n).

## Complejidad

- Tiempo: O(log n)
- Espacio: O(1)
