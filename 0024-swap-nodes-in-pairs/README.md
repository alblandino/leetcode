# 24. Swap Nodes in Pairs

- **Dificultad:** Media
- **Enlace:** https://leetcode.com/problems/swap-nodes-in-pairs/

## Problema

Se recibe una lista enlazada y hay que intercambiar los nodos de a pares: el primero con el segundo, el tercero con el cuarto, y asi. Si la cantidad de nodos es impar, el ultimo queda en su lugar. Se devuelve la nueva cabeza.

No vale cambiar los valores guardados en los nodos, hay que mover los nodos mismos cambiando sus enlaces.

## Ejemplos

```
Entrada: head = [1,2,3,4]
Salida: [2,1,4,3]
```

```
Entrada: head = []
Salida: []
```

```
Entrada: head = [1,2,3]
Salida: [2,1,3]
```

El 3 no tiene pareja y se queda al final.

## Restricciones

- La cantidad de nodos de la lista esta en el rango `[0, 100]`.
- `0 <= Node.val <= 100`

## Solucion

Se usa un nodo ficticio antes de la cabeza y un puntero `prev` al nodo que esta justo antes del par que toca. Mientras haya dos nodos despues de `prev` (`first` y `second`), se reconectan en tres pasos: `first` apunta a lo que venia despues de `second`, `second` apunta a `first`, y `prev` apunta a `second`.

Despues del cambio `first` quedo segundo en el par, asi que pasa a ser el nuevo `prev` para el siguiente par. El nodo ficticio permite tratar el primer par igual que los demas, aunque cambie la cabeza.

Tambien se puede resolver con recursion, pero esa version usa O(n) de pila. La version iterativa usa memoria constante.

## Complejidad

- Tiempo: O(n)
- Espacio: O(1)
