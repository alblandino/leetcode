# 99. Recover Binary Search Tree

- **Dificultad:** Media
- **Enlace:** https://leetcode.com/problems/recover-binary-search-tree/

## Problema

Se recibe un arbol binario de busqueda en el que, por error, se intercambiaron los valores de exactamente dos nodos. Hay que arreglarlo devolviendo esos dos valores a su lugar.

La forma del arbol no se puede cambiar: solo se corrigen valores. La funcion no devuelve nada, modifica el arbol que recibe.

## Ejemplos

```
Entrada: root = [1,3,null,null,2]
Salida: [3,1,null,null,2]
```

El 3 no puede ser hijo izquierdo del 1; al intercambiar 1 y 3 el arbol vuelve a ser valido.

```
Entrada: root = [3,1,4,null,null,2]
Salida: [2,1,4,null,null,3]
```

El 2 no puede estar a la derecha del 3; se intercambian 2 y 3.

## Restricciones

- El numero de nodos del arbol esta en el rango `[2, 1000]`.
- `-2^31 <= Node.val <= 2^31 - 1`

## Solucion

En un BST correcto el recorrido inorden sale ordenado. Si se intercambian dos valores, en ese recorrido aparecen uno o dos lugares donde un valor es mayor que el siguiente. El primer nodo fuera de lugar es el de mayor valor en la primera bajada, y el segundo es el de menor valor en la ultima bajada. Si los nodos intercambiados estaban seguidos en el recorrido, hay una sola bajada y ambos salen de ella.

Se recorre el arbol en inorden de forma iterativa, guardando el nodo anterior, se anotan los dos nodos y al final se intercambian sus valores. El follow up pide espacio O(1), que se logra con el recorrido de Morris; aqui se usa la pila, que es mas facil de leer y suficiente para 1000 nodos.

## Complejidad

- Tiempo: O(n)
- Espacio: O(h), donde h es la altura del arbol
