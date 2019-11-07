# 88. Merge Sorted Array

- **Dificultad:** Facil
- **Enlace:** https://leetcode.com/problems/merge-sorted-array/

## Problema

Se tienen dos arreglos ordenados de menor a mayor, `nums1` y `nums2`, con `m` y `n` elementos utiles. Hay que mezclarlos en un solo arreglo ordenado.

La funcion no devuelve nada: el resultado tiene que quedar dentro de `nums1`. Para eso `nums1` ya tiene largo `m + n`, con los `m` numeros reales al inicio y `n` ceros de relleno al final.

## Ejemplos

```
Entrada: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Salida: [1,2,2,3,5,6]
```

```
Entrada: nums1 = [1], m = 1, nums2 = [], n = 0
Salida: [1]
```

```
Entrada: nums1 = [0], m = 0, nums2 = [1], n = 1
Salida: [1]
```

Con `m = 0` el 0 de `nums1` es solo relleno y no cuenta como elemento.

## Restricciones

- `nums1.length == m + n`
- `nums2.length == n`
- `0 <= m, n <= 200`
- `1 <= m + n <= 200`
- `-10^9 <= nums1[i], nums2[j] <= 10^9`

## Solucion

Se llena `nums1` desde el final hacia el inicio con tres punteros: el ultimo elemento real de `nums1`, el ultimo de `nums2` y la posicion donde se escribe. En cada paso se pone el mayor de los dos candidatos en la posicion de escritura y se retrocede.

Ir desde atras evita pisar valores de `nums1` que todavia no se han usado, porque el espacio libre esta al final. Cuando `nums2` se termina, lo que queda de `nums1` ya esta en su lugar. Juntar todo y ordenar funcionaria, pero seria O((m + n) log(m + n)) y no aprovecha que ya vienen ordenados.

## Complejidad

- Tiempo: O(m + n)
- Espacio: O(1)
