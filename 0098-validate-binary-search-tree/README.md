# 98. Validate Binary Search Tree

- **Dificultad:** Media
- **Enlace:** https://leetcode.com/problems/validate-binary-search-tree/

## Problema

Se recibe la raiz de un arbol binario y hay que decir si es un arbol binario de busqueda (BST) valido.

Para eso, en cada nodo todos los valores de su subarbol izquierdo tienen que ser estrictamente menores que el, y todos los de su subarbol derecho estrictamente mayores. No basta con mirar a los hijos directos: la regla aplica a todo el subarbol. Valores repetidos no se permiten.

## Ejemplos

```
Entrada: root = [2,1,3]
Salida: true
```

```
Entrada: root = [5,1,4,null,null,3,6]
Salida: false
```

El hijo derecho de la raiz 5 es 4, que es menor que 5.

## Restricciones

- El numero de nodos del arbol esta en el rango `[1, 10^4]`.
- `-2^31 <= Node.val <= 2^31 - 1`

## Solucion

Un arbol es un BST valido si y solo si su recorrido inorden (izquierda, nodo, derecha) sale estrictamente creciente. Se hace ese recorrido de forma iterativa con una pila y se compara cada valor con el anterior; si alguno es menor o igual, el arbol no es valido y se corta ahi.

El error comun es comparar cada nodo solo con sus hijos, lo que acepta arboles como `[5,4,6,null,null,3,7]`, donde el 3 esta a la derecha del 5. El recorrido inorden detecta ese caso. Se usa la version iterativa porque el arbol puede tener 10^4 nodos en una sola rama, y la recursion pasaria el limite por defecto de Python.

## Complejidad

- Tiempo: O(n)
- Espacio: O(h), donde h es la altura del arbol
