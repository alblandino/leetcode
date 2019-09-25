# 75. Sort Colors

- **Dificultad:** Media
- **Enlace:** https://leetcode.com/problems/sort-colors/

## Problema

Se recibe un arreglo `nums` con valores 0, 1 y 2, que representan los colores rojo, blanco y azul. Hay que ordenarlo en el lugar para que queden primero todos los 0, despues los 1 y al final los 2.

No se puede usar la funcion de ordenamiento de la libreria, y el metodo no devuelve nada: modifica `nums`.

## Ejemplos

```
Entrada: nums = [2,0,2,1,1,0]
Salida: [0,0,1,1,2,2]
```

```
Entrada: nums = [2,0,1]
Salida: [0,1,2]
```

## Restricciones

- `n == nums.length`
- `1 <= n <= 300`
- `nums[i]` es 0, 1 o 2.

## Solucion

Algoritmo de la bandera holandesa (Dijkstra), en una sola pasada. Se usan tres indices: `low` marca donde va el proximo 0, `high` donde va el proximo 2 y `mid` recorre el arreglo. Todo lo que esta antes de `low` son 0, entre `low` y `mid` son 1 y despues de `high` son 2.

Si `nums[mid]` es 0, se intercambia con `nums[low]` y avanzan los dos. Si es 1, solo avanza `mid`. Si es 2, se intercambia con `nums[high]` y baja `high`, pero `mid` no avanza porque el valor que llego desde atras todavia no se reviso. Contar cuantos 0, 1 y 2 hay y reescribir el arreglo tambien funciona, pero necesita dos pasadas.

## Complejidad

- Tiempo: O(n)
- Espacio: O(1)
