# 40. Combination Sum II

- **Dificultad:** Media
- **Enlace:** https://leetcode.com/problems/combination-sum-ii/

## Problema

Se recibe una lista `candidates` (que puede tener numeros repetidos) y un numero `target`. Hay que encontrar todas las combinaciones que suman `target` usando cada posicion de la lista a lo mas una vez.

El resultado no puede tener dos combinaciones iguales, aunque se hayan armado con copias distintas del mismo numero.

## Ejemplos

```
Entrada: candidates = [10,1,2,7,6,1,5], target = 8
Salida: [[1,1,6],[1,2,5],[1,7],[2,6]]
```

```
Entrada: candidates = [2,5,2,1,2], target = 5
Salida: [[1,2,2],[5]]
```

Hay tres 2, pero la combinacion [1,2,2] aparece una sola vez.

## Restricciones

- `1 <= candidates.length <= 100`
- `1 <= candidates[i] <= 50`
- `1 <= target <= 30`

## Solucion

Es el mismo backtracking que en Combination Sum, con dos cambios. Primero, al bajar en la recursion se pasa `i + 1`, porque cada posicion se usa una sola vez. Segundo, para no repetir combinaciones se ordena la lista y, dentro de un mismo nivel de la recursion, se salta un numero si es igual al anterior (`i > start and nums[i] == nums[i - 1]`): la primera copia ya exploro todas las combinaciones que empiezan con ese valor en esa posicion.

Generar todo y quitar duplicados con un set al final tambien funciona, pero explora muchas ramas repetidas. Como la lista esta ordenada, tambien se corta el ciclo cuando un numero ya es mayor que lo que falta.

## Complejidad

- Tiempo: O(2^n * n) en el peor caso
- Espacio: O(n) por la profundidad de la recursion y la copia ordenada, sin contar la salida
