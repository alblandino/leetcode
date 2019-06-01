# 39. Combination Sum

- **Dificultad:** Media
- **Enlace:** https://leetcode.com/problems/combination-sum/

## Problema

Se recibe una lista `candidates` de enteros distintos y un numero `target`. Hay que encontrar todas las combinaciones de numeros de la lista cuya suma sea `target`. Cada numero se puede usar las veces que se quiera.

Dos combinaciones cuentan como distintas solo si algun numero aparece una cantidad diferente de veces (el orden no importa). Las combinaciones se pueden devolver en cualquier orden.

## Ejemplos

```
Entrada: candidates = [2,3,6,7], target = 7
Salida: [[2,2,3],[7]]
```

2 + 2 + 3 = 7 usando el 2 dos veces, y el 7 solo ya suma 7.

```
Entrada: candidates = [2,3,5], target = 8
Salida: [[2,2,2,2],[2,3,3],[3,5]]
```

```
Entrada: candidates = [2], target = 1
Salida: []
```

## Restricciones

- `1 <= candidates.length <= 30`
- `2 <= candidates[i] <= 40`
- Todos los elementos de `candidates` son distintos.
- `1 <= target <= 40`

## Solucion

Se usa backtracking sobre la lista ordenada. La funcion recursiva recibe desde que indice puede elegir y cuanto falta para llegar a `target`. Para cada candidato desde ese indice lo agrega al camino y se llama a si misma con el mismo indice (porque el numero se puede repetir) y con lo que falta reducido. Cuando lo que falta llega a 0 se guarda una copia del camino.

Empezar siempre desde el indice actual, y no desde 0, evita generar la misma combinacion en otro orden. Como la lista esta ordenada, en cuanto un candidato es mayor que lo que falta se corta el ciclo, porque los siguientes tambien lo seran.

## Complejidad

- Tiempo: O(n^(T/M + 1)) en el peor caso, donde n es la cantidad de candidatos, T es `target` y M el candidato mas pequeno
- Espacio: O(T/M) por la profundidad de la recursion, sin contar la salida
