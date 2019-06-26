# 46. Permutations

- **Dificultad:** Media
- **Enlace:** https://leetcode.com/problems/permutations/

## Problema

Se recibe un arreglo `nums` de enteros sin repetidos. Hay que devolver todas las formas posibles de ordenar sus elementos.

Las permutaciones se pueden devolver en cualquier orden.

## Ejemplos

```
Entrada: nums = [1,2,3]
Salida: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
```

```
Entrada: nums = [0,1]
Salida: [[0,1],[1,0]]
```

```
Entrada: nums = [1]
Salida: [[1]]
```

## Restricciones

- `1 <= nums.length <= 6`
- `-10 <= nums[i] <= 10`
- Todos los enteros de `nums` son distintos.

## Solucion

Se usa backtracking. Se arma la permutacion en una lista `path` y se lleva un arreglo `used` que marca que posiciones de `nums` ya estan en el camino. En cada nivel se prueba cada numero no usado: se agrega, se marca, se baja un nivel y al volver se deshace. Cuando `path` tiene todos los numeros se guarda una copia.

Hay `n!` permutaciones y cada una tiene `n` elementos, asi que no se puede hacer mejor que O(n * n!). `itertools.permutations` haria lo mismo, pero en una entrevista se espera ver el backtracking.

## Complejidad

- Tiempo: O(n * n!)
- Espacio: O(n) por la recursion, `path` y `used`, sin contar la salida
