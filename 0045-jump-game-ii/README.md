# 45. Jump Game II

- **Dificultad:** Media
- **Enlace:** https://leetcode.com/problems/jump-game-ii/

## Problema

Se recibe un arreglo `nums` y se empieza parado en el indice 0. El valor `nums[i]` es lo mas lejos que se puede saltar hacia adelante desde la posicion `i` (se puede saltar menos). Hay que devolver la menor cantidad de saltos para llegar al ultimo indice.

Siempre es posible llegar al final.

## Ejemplos

```
Entrada: nums = [2,3,1,1,4]
Salida: 2
```

Se salta del indice 0 al 1, y desde ahi 3 posiciones hasta el final.

```
Entrada: nums = [2,3,0,1,4]
Salida: 2
```

## Restricciones

- `1 <= nums.length <= 10^4`
- `0 <= nums[i] <= 1000`
- Se garantiza que se puede llegar a `nums[n - 1]`.

## Solucion

Se piensa como una busqueda por niveles: con 1 salto se llega a cierto rango de indices, con 2 saltos a otro rango mas amplio, y asi. Se recorre el arreglo guardando `current_end` (el ultimo indice alcanzable con los saltos actuales) y `farthest` (lo mas lejos que se llega con un salto mas desde cualquier indice ya visto). Cuando `i` llega a `current_end`, se agota el rango actual: se cuenta un salto y el nuevo limite pasa a ser `farthest`.

El recorrido se detiene antes del ultimo indice, porque al llegar ahi ya no hace falta saltar. Una tabla dp que para cada indice revise todos los saltos posibles seria O(n^2); este enfoque greedy lo hace en una pasada.

## Complejidad

- Tiempo: O(n)
- Espacio: O(1)
