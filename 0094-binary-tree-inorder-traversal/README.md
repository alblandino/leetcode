# 94. Binary Tree Inorder Traversal

- **Dificultad:** Facil
- **Enlace:** https://leetcode.com/problems/binary-tree-inorder-traversal/

## Problema

Se recibe la raiz de un arbol binario y hay que devolver sus valores en recorrido inorden: primero todo el subarbol izquierdo, despues el nodo, despues todo el subarbol derecho, aplicando esa regla en cada nodo.

El arbol puede estar vacio, y en ese caso se devuelve una lista vacia.

## Ejemplos

```
Entrada: root = [1,null,2,3]
Salida: [1,3,2]
```

El 1 no tiene hijo izquierdo, su hijo derecho es el 2 y el 3 es hijo izquierdo del 2.

```
Entrada: root = [1,2,3,4,5,null,8,null,null,6,7,9]
Salida: [4,2,6,5,7,1,3,9,8]
```

```
Entrada: root = []
Salida: []
```

## Restricciones

- El numero de nodos del arbol esta en el rango `[0, 100]`.
- `-100 <= Node.val <= 100`

## Solucion

La version recursiva es directa, asi que se hace la iterativa que pide el follow up, con una pila explicita. Desde el nodo actual se baja por la izquierda todo lo posible, guardando cada nodo en la pila. Cuando ya no hay hijo izquierdo, se saca el tope de la pila, se agrega su valor y se pasa a su hijo derecho, repitiendo lo mismo desde ahi.

La pila hace el trabajo que haria la pila de llamadas en la version recursiva: recuerda los nodos cuyo valor todavia no se ha visitado porque falta terminar su lado izquierdo.

## Complejidad

- Tiempo: O(n)
- Espacio: O(h), donde h es la altura del arbol (O(n) si esta desbalanceado)
