# 19. Remove Nth Node From End of List

- **Dificultad:** Media
- **Enlace:** https://leetcode.com/problems/remove-nth-node-from-end-of-list/

## Problema

Se recibe la cabeza de una lista enlazada y un numero `n`. Hay que quitar el nodo que esta en la posicion `n` contando desde el final (el ultimo es el 1) y devolver la cabeza de la lista que queda.

`n` siempre es valido, es decir, nunca es mayor que el largo de la lista. Como reto, el enunciado propone hacerlo recorriendo la lista una sola vez.

## Ejemplos

```
Entrada: head = [1,2,3,4,5], n = 2
Salida: [1,2,3,5]
```

El segundo desde el final es el 4.

```
Entrada: head = [1], n = 1
Salida: []
```

```
Entrada: head = [1,2], n = 1
Salida: [1]
```

## Restricciones

- La cantidad de nodos de la lista es `sz`.
- `1 <= sz <= 30`
- `0 <= Node.val <= 100`
- `1 <= n <= sz`

## Solucion

Se usan dos punteros, `fast` y `slow`, que empiezan en un nodo ficticio puesto antes de la cabeza. Primero `fast` avanza `n + 1` pasos, asi queda una distancia fija entre los dos. Despues avanzan juntos hasta que `fast` se sale de la lista.

En ese momento `slow` esta justo antes del nodo a borrar, y basta con saltarlo: `slow.next = slow.next.next`. El nodo ficticio cubre el caso en que hay que borrar la cabeza, porque `slow` puede quedarse antes de ella.

La forma directa es contar el largo en una pasada y borrar en otra. Tiene la misma complejidad, pero con dos punteros se hace en una sola pasada como pide el reto.

## Complejidad

- Tiempo: O(sz)
- Espacio: O(1)
