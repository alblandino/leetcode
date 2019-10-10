# 80. Remove Duplicates from Sorted Array II

- **Dificultad:** Media
- **Enlace:** https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/

## Problema

Se recibe un arreglo `nums` ordenado de menor a mayor. Hay que dejar cada valor como maximo dos veces, sin cambiar el orden, y hacerlo sobre el mismo arreglo, sin crear otro y usando memoria extra constante.

La funcion devuelve `k`, la cantidad de elementos que quedan. Esos `k` elementos deben estar en las primeras `k` posiciones de `nums`; lo que quede despues no importa.

## Ejemplos

```
Entrada: nums = [1,1,1,2,2,3]
Salida: 5, nums = [1,1,2,2,3,_]
```

```
Entrada: nums = [0,0,1,1,1,1,2,3,3]
Salida: 7, nums = [0,0,1,1,2,3,3,_,_]
```

El `_` marca posiciones cuyo valor no importa.

## Restricciones

- `1 <= nums.length <= 3 * 10^4`
- `-10^4 <= nums[i] <= 10^4`
- `nums` esta ordenado de forma no decreciente.

## Solucion

Se usan dos punteros: uno recorre el arreglo y otro (`write`) marca donde va el siguiente numero que se queda. Un numero se puede quedar si todavia no hay dos elementos escritos, o si es distinto al que esta dos posiciones antes de `write`.

Como el arreglo esta ordenado, si el numero es igual al que esta dos lugares atras en la parte ya escrita, significa que ya hay dos copias y esta seria la tercera, asi que se salta. Al final `write` es justamente `k`.

## Complejidad

- Tiempo: O(n)
- Espacio: O(1)
