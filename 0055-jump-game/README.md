# 55. Jump Game

- **Dificultad:** Media
- **Enlace:** https://leetcode.com/problems/jump-game/

## Problema

Se empieza en la primera posicion de un arreglo `nums`. El valor de cada posicion dice cuantos pasos como maximo se pueden saltar hacia adelante desde ahi (se puede saltar menos).

Hay que decidir si es posible llegar a la ultima posicion del arreglo.

## Ejemplos

```
Entrada: nums = [2,3,1,1,4]
Salida: true
```

Se salta 1 paso hasta el indice 1 y desde ahi 3 pasos hasta el final.

```
Entrada: nums = [3,2,1,0,4]
Salida: false
```

Todos los caminos terminan en el indice 3, que tiene un 0 y no deja avanzar.

## Restricciones

- `1 <= nums.length <= 10^4`
- `0 <= nums[i] <= 10^5`

## Solucion

Enfoque greedy. Se recorre el arreglo guardando el indice mas lejano al que se puede llegar hasta ahora (`farthest`). Si el indice actual es mayor que `farthest`, esa posicion es inalcanzable y la respuesta es falso. Si no, se actualiza `farthest` con `i + nums[i]`. Si `farthest` llega a la ultima posicion, la respuesta es verdadero.

Funciona porque todas las posiciones hasta `farthest` son alcanzables, asi que basta con saber hasta donde llega el mejor salto visto. Una solucion con programacion dinamica o probando todos los saltos seria O(n^2).

## Complejidad

- Tiempo: O(n)
- Espacio: O(1)
