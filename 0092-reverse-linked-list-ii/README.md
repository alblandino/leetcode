# 92. Reverse Linked List II

- **Dificultad:** Media
- **Enlace:** https://leetcode.com/problems/reverse-linked-list-ii/

## Problema

Se recibe una lista enlazada y dos posiciones `left` y `right` (contando desde 1, con `left <= right`). Hay que invertir solo el tramo de nodos entre esas dos posiciones, incluidas, y dejar el resto de la lista igual.

Se devuelve la cabeza de la lista ya modificada, que cambia si el tramo empieza en la posicion 1.

## Ejemplos

```
Entrada: head = [1,2,3,4,5], left = 2, right = 4
Salida: [1,4,3,2,5]
```

```
Entrada: head = [5], left = 1, right = 1
Salida: [5]
```

## Restricciones

- El numero de nodos de la lista es `n`.
- `1 <= n <= 500`
- `-500 <= Node.val <= 500`
- `1 <= left <= right <= n`

## Solucion

Se pone un nodo ficticio antes de la cabeza para que el caso `left = 1` no sea especial. Se avanza hasta `before`, el nodo justo antes del tramo.

Desde ahi se invierte el tramo como una lista normal, con `prev` y `current`, durante `right - left + 1` pasos. Al terminar, `prev` es el nuevo primer nodo del tramo y `current` es el nodo que venia despues de el. Solo falta reconectar: el que antes era el primero del tramo (ahora el ultimo) apunta a `current`, y `before` apunta a `prev`.

Todo se hace en una sola pasada, que es lo que pide el follow up.

## Complejidad

- Tiempo: O(n)
- Espacio: O(1)
