# 23. Merge k Sorted Lists

- **Dificultad:** Dificil
- **Enlace:** https://leetcode.com/problems/merge-k-sorted-lists/

## Problema

Se recibe un arreglo con `k` listas enlazadas, cada una ordenada de menor a mayor. Hay que unirlas todas en una sola lista ordenada y devolver su cabeza.

El arreglo puede venir vacio y algunas listas pueden no tener nodos. En esos casos el resultado tambien puede ser una lista vacia.

## Ejemplos

```
Entrada: lists = [[1,4,5],[1,3,4],[2,6]]
Salida: [1,1,2,3,4,4,5,6]
```

```
Entrada: lists = []
Salida: []
```

```
Entrada: lists = [[]]
Salida: []
```

Hay una lista, pero esta vacia.

## Restricciones

- `k == lists.length`
- `0 <= k <= 10^4`
- `0 <= lists[i].length <= 500`
- `-10^4 <= lists[i][j] <= 10^4`
- `lists[i]` esta ordenada de forma ascendente.
- La suma de todos los `lists[i].length` no pasa de `10^4`.

## Solucion

En cada paso el siguiente nodo del resultado es el menor entre las cabezas actuales de las `k` listas. Para encontrarlo rapido se guardan esas cabezas en un min-heap (`heapq`). Se saca la menor, se engancha al final del resultado y, si ese nodo tiene siguiente, se mete el siguiente al heap.

En el heap se guardan tuplas `(valor, indice de la lista, nodo)`. El indice sirve de desempate cuando dos valores son iguales, para que Python no intente comparar dos `ListNode`. Como cada lista tiene a lo sumo un nodo dentro del heap, nunca hay dos tuplas con el mismo valor y el mismo indice.

Buscar el minimo recorriendo las `k` cabezas en cada paso costaria O(N * k). Mezclar las listas de a una con la primera tambien llega a O(N * k). El heap baja cada paso a O(log k).

## Complejidad

- Tiempo: O(N log k), donde N es el total de nodos
- Espacio: O(k) por el heap
