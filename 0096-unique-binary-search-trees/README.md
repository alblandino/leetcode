# 96. Unique Binary Search Trees

- **Dificultad:** Media
- **Enlace:** https://leetcode.com/problems/unique-binary-search-trees/

## Problema

Dado `n`, hay que contar cuantos arboles binarios de busqueda (BST) con forma distinta se pueden armar usando exactamente los valores de 1 a `n`.

Es la version que solo cuenta del problema 95: no hace falta construir los arboles.

## Ejemplos

```
Entrada: n = 3
Salida: 5
```

```
Entrada: n = 1
Salida: 1
```

## Restricciones

- `1 <= n <= 19`

## Solucion

La cantidad de BST no depende de que valores sean, solo de cuantos son. Si se elige el valor `root` como raiz entre `nodes` valores, a la izquierda quedan `root - 1` valores y a la derecha `nodes - root`, y cada lado se arma de forma independiente. Entonces las formas con esa raiz son `count[root - 1] * count[nodes - root]`.

Con eso se llena una tabla `count` desde 0 nodos (un solo arbol, el vacio) hasta `n`, sumando sobre todas las raices posibles. Estos valores son los numeros de Catalan.

Construir los arboles como en el problema 95 para contarlos seria mucho mas lento: para `n = 19` hay mas de 1700 millones.

## Complejidad

- Tiempo: O(n^2)
- Espacio: O(n)
