# 83. Remove Duplicates from Sorted List

- **Dificultad:** Facil
- **Enlace:** https://leetcode.com/problems/remove-duplicates-from-sorted-list/

## Problema

Se recibe la cabeza de una lista enlazada ordenada. Hay que quitar las copias repetidas para que cada valor quede una sola vez, y devolver la lista, que sigue ordenada.

A diferencia del problema 82, aqui si se conserva una copia de cada valor repetido.

## Ejemplos

```
Entrada: head = [1,1,2]
Salida: [1,2]
```

```
Entrada: head = [1,1,2,3,3]
Salida: [1,2,3]
```

## Restricciones

- El numero de nodos de la lista esta en el rango `[0, 300]`.
- `-100 <= Node.val <= 100`
- Se garantiza que la lista esta ordenada de forma ascendente.

## Solucion

Como la lista esta ordenada, los valores iguales estan uno junto al otro. Se recorre con un puntero: si el siguiente nodo tiene el mismo valor que el actual, se salta (el actual pasa a apuntar al que viene despues); si es distinto, se avanza.

No hace falta un nodo ficticio porque la cabeza nunca se borra: siempre se queda la primera copia de cada valor.

## Complejidad

- Tiempo: O(n)
- Espacio: O(1)
