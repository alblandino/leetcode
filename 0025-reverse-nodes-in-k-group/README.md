# 25. Reverse Nodes in k-Group

- **Dificultad:** Dificil
- **Enlace:** https://leetcode.com/problems/reverse-nodes-in-k-group/

## Problema

Se recibe la cabeza de una lista enlazada y un entero `k`. Hay que dividir la lista en bloques consecutivos de `k` nodos e invertir el orden dentro de cada bloque. Si al final sobran menos de `k` nodos, esos se dejan tal como estan.

Igual que en el problema de intercambiar pares, no se pueden cambiar los valores de los nodos, solo sus enlaces. Como reto, el enunciado propone usar memoria extra O(1).

## Ejemplos

```
Entrada: head = [1,2,3,4,5], k = 2
Salida: [2,1,4,3,5]
```

```
Entrada: head = [1,2,3,4,5], k = 3
Salida: [3,2,1,4,5]
```

Se invierte el bloque [1,2,3]; con [4,5] no alcanza para otro bloque y se deja igual.

## Restricciones

- La cantidad de nodos de la lista es `n`.
- `1 <= k <= n <= 5000`
- `0 <= Node.val <= 1000`

## Solucion

Se trabaja bloque por bloque con un nodo ficticio antes de la cabeza y un puntero `group_prev` al nodo que queda justo antes del bloque actual. Primero se busca el nodo numero `k` desde `group_prev` (`kth`). Si no existe, quedan menos de `k` nodos y se termina.

Si existe, se invierte el bloque con la tecnica de siempre para listas (`prev`, `current`, `next_node`), pero empezando con `prev = kth.next`, asi el primer nodo del bloque queda apuntando directo a lo que sigue. Luego `group_prev` se conecta a `kth`, que es la nueva cabeza del bloque, y el antiguo primer nodo, que ahora es el ultimo, pasa a ser el `group_prev` del siguiente bloque.

Copiar los valores a un arreglo e invertir por tramos seria mas facil, pero usa O(n) de memoria y ademas cambia valores en vez de nodos. Asi se cumple el reto de memoria O(1).

## Complejidad

- Tiempo: O(n), cada nodo se visita un par de veces
- Espacio: O(1)
