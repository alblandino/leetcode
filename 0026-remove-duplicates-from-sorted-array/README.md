# 26. Remove Duplicates from Sorted Array

- **Dificultad:** Facil
- **Enlace:** https://leetcode.com/problems/remove-duplicates-from-sorted-array/

## Problema

Se recibe un arreglo `nums` ordenado de menor a mayor que puede tener valores repetidos. Hay que dejar cada valor una sola vez al inicio del mismo arreglo, sin crear otro y respetando el orden original.

La funcion devuelve `k`, la cantidad de valores distintos. Solo se revisan las primeras `k` posiciones de `nums`; lo que quede despues no importa.

## Ejemplos

```
Entrada: nums = [1,1,2]
Salida: 2, nums = [1,2,_]
```

```
Entrada: nums = [0,0,1,1,1,2,2,3,3,4]
Salida: 5, nums = [0,1,2,3,4,_,_,_,_,_]
```

El `_` marca posiciones cuyo valor no se revisa.

## Restricciones

- `1 <= nums.length <= 3 * 10^4`
- `-100 <= nums[i] <= 100`
- `nums` esta ordenado de forma no decreciente.

## Solucion

Se usan dos punteros: `k` marca donde se escribe el siguiente valor unico e `i` recorre el arreglo. Como el arreglo esta ordenado, los repetidos quedan juntos, asi que basta comparar `nums[i]` con el ultimo valor escrito (`nums[k - 1]`). Si es distinto, se copia en la posicion `k` y `k` avanza.

Un set o un arreglo nuevo tambien darian la respuesta, pero usan memoria extra y el problema pide modificar el mismo arreglo.

## Complejidad

- Tiempo: O(n)
- Espacio: O(1)
