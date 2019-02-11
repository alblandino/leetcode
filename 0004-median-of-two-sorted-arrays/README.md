# 4. Median of Two Sorted Arrays

- **Dificultad:** Dificil
- **Enlace:** https://leetcode.com/problems/median-of-two-sorted-arrays/

## Problema

Se reciben dos arreglos ya ordenados, `nums1` de tamano `m` y `nums2` de tamano `n`. Hay que devolver la mediana de todos sus numeros juntos, como si fueran un solo arreglo ordenado.

Si el total de numeros es impar, la mediana es el del medio. Si es par, es el promedio de los dos del medio. El enunciado pide hacerlo en O(log (m + n)).

## Ejemplos

```
Entrada: nums1 = [1,3], nums2 = [2]
Salida: 2.00000
```

Juntos quedan [1,2,3] y el del medio es 2.

```
Entrada: nums1 = [1,2], nums2 = [3,4]
Salida: 2.50000
```

Juntos quedan [1,2,3,4] y la mediana es (2 + 3) / 2.

## Restricciones

- `nums1.length == m`
- `nums2.length == n`
- `0 <= m <= 1000`
- `0 <= n <= 1000`
- `1 <= m + n <= 2000`
- `-10^6 <= nums1[i], nums2[i] <= 10^6`

## Solucion

La idea es partir los dos arreglos en una mitad izquierda y una derecha sin mezclarlos. Si se toman `cut1` elementos de `nums1` y `cut2 = half - cut1` de `nums2`, la mitad izquierda siempre tiene `half = (m + n + 1) // 2` elementos. El corte es correcto cuando el ultimo de la izquierda de cada arreglo es menor o igual que el primero de la derecha del otro (`left1 <= right2` y `left2 <= right1`).

Se hace busqueda binaria sobre `cut1` en el arreglo mas corto: si `left1 > right2` se tomaron demasiados de `nums1` y hay que mover el corte a la izquierda; si no, a la derecha. Cuando un corte queda en un extremo se usa `-inf` o `inf` para no salirse del arreglo. Con el corte correcto, la mediana sale de `max(left1, left2)` (total impar) o del promedio de ese valor con `min(right1, right2)` (total par).

Mezclar los arreglos como en merge sort es mas facil pero cuesta O(m + n), que no cumple lo que pide el enunciado.

## Complejidad

- Tiempo: O(log(min(m, n)))
- Espacio: O(1)
