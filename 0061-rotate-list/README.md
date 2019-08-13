# 61. Rotate List

- **Dificultad:** Media
- **Enlace:** https://leetcode.com/problems/rotate-list/

## Problema

Se recibe la cabeza de una lista enlazada y un entero `k`. Hay que rotar la lista `k` posiciones a la derecha: en cada rotacion el ultimo nodo pasa a ser el primero. Se devuelve la nueva cabeza.

`k` puede ser mucho mas grande que el largo de la lista.

## Ejemplos

```
Entrada: head = [1,2,3,4,5], k = 2
Salida: [4,5,1,2,3]
```

```
Entrada: head = [0,1,2], k = 4
Salida: [2,0,1]
```

Rotar 3 veces una lista de 3 nodos la deja igual, asi que 4 rotaciones equivalen a 1.

## Restricciones

- El numero de nodos de la lista esta en el rango `[0, 500]`.
- `-100 <= Node.val <= 100`
- `0 <= k <= 2 * 10^9`

## Solucion

Primero se recorre la lista para saber su largo y encontrar el ultimo nodo. Como rotar `length` veces deja la lista igual, solo importa `k % length`. Si eso da 0 se devuelve la lista sin cambios.

Si no, la nueva cola es el nodo en la posicion `length - k - 1` y la nueva cabeza es el que le sigue. Se corta la lista despues de la nueva cola y el antiguo ultimo nodo se conecta con la antigua cabeza. Rotar de a un paso `k` veces seria O(n * k), inviable con `k` de hasta `2 * 10^9`.

## Complejidad

- Tiempo: O(n)
- Espacio: O(1)
