# 21. Merge Two Sorted Lists

- **Dificultad:** Facil
- **Enlace:** https://leetcode.com/problems/merge-two-sorted-lists/

## Problema

Se reciben las cabezas de dos listas enlazadas, `list1` y `list2`, cada una ordenada de menor a mayor. Hay que unirlas en una sola lista ordenada y devolver su cabeza.

La lista nueva se arma reutilizando los nodos que ya existen, cambiando sus enlaces, no copiando los valores. Cualquiera de las dos listas puede venir vacia.

## Ejemplos

```
Entrada: list1 = [1,2,4], list2 = [1,3,4]
Salida: [1,1,2,3,4,4]
```

```
Entrada: list1 = [], list2 = []
Salida: []
```

```
Entrada: list1 = [], list2 = [0]
Salida: [0]
```

## Restricciones

- La cantidad de nodos de ambas listas esta en el rango `[0, 50]`.
- `-100 <= Node.val <= 100`
- `list1` y `list2` estan ordenadas de forma no decreciente.

## Solucion

Es el paso de mezcla de merge sort. Se usa un nodo ficticio como inicio y un puntero `tail` al ultimo nodo del resultado. Mientras las dos listas tengan nodos, se compara la cabeza de cada una, se engancha la menor detras de `tail` y se avanza en esa lista.

Cuando una lista se termina, la otra ya esta ordenada, asi que se engancha completa de una sola vez. El nodo ficticio evita tener que decidir aparte cual es la cabeza del resultado.

## Complejidad

- Tiempo: O(m + n)
- Espacio: O(1), solo se cambian enlaces
