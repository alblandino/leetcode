# 47. Permutations II

- **Dificultad:** Media
- **Enlace:** https://leetcode.com/problems/permutations-ii/

## Problema

Se recibe un arreglo `nums` que puede tener numeros repetidos. Hay que devolver todas las formas distintas de ordenar sus elementos, sin repetir ninguna.

Las permutaciones se pueden devolver en cualquier orden.

## Ejemplos

```
Entrada: nums = [1,1,2]
Salida: [[1,1,2],[1,2,1],[2,1,1]]
```

Aunque hay dos 1, cada orden aparece una sola vez.

```
Entrada: nums = [1,2,3]
Salida: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
```

## Restricciones

- `1 <= nums.length <= 8`
- `-10 <= nums[i] <= 10`

## Solucion

Es el backtracking de Permutations con una regla extra para los repetidos. Se ordena el arreglo para que los valores iguales queden juntos. Al elegir el siguiente numero, se salta `nums[i]` si es igual a `nums[i - 1]` y `nums[i - 1]` todavia no esta usado. Asi las copias de un mismo valor siempre entran en el mismo orden (primero la de la izquierda), y cada permutacion se genera una sola vez.

Generar todas las permutaciones y filtrarlas con un set tambien funciona, pero recorre ramas repetidas y gasta memoria en el set. Con la regla se cortan esas ramas desde el inicio.

## Complejidad

- Tiempo: O(n * n!) en el peor caso (cuando no hay repetidos)
- Espacio: O(n) por la recursion, `path` y `used`, sin contar la salida
