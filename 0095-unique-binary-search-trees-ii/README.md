# 95. Unique Binary Search Trees II

- **Dificultad:** Media
- **Enlace:** https://leetcode.com/problems/unique-binary-search-trees-ii/

## Problema

Dado `n`, hay que construir todos los arboles binarios de busqueda (BST) distintos que usan exactamente los valores de 1 a `n`, cada uno una vez. Dos arboles cuentan como distintos si tienen forma distinta.

Se devuelve una lista con la raiz de cada arbol, en cualquier orden.

## Ejemplos

```
Entrada: n = 3
Salida: [[1,null,2,null,3],[1,null,3,2],[2,1,3],[3,1,null,null,2],[3,2,null,1]]
```

Con 3 valores hay 5 BST posibles, escritos aqui en orden por niveles.

```
Entrada: n = 1
Salida: [[1]]
```

## Restricciones

- `1 <= n <= 8`

## Solucion

Recursion sobre rangos. Para construir todos los BST con los valores de `low` a `high`, se prueba cada valor `root_val` del rango como raiz. Por la regla del BST, a su izquierda solo pueden ir los valores menores (`low` a `root_val - 1`) y a su derecha los mayores (`root_val + 1` a `high`).

Se generan recursivamente todos los subarboles izquierdos y todos los derechos, y se combina cada izquierdo con cada derecho bajo una nueva raiz. Un rango vacio devuelve `[None]`, que representa el arbol vacio y permite que la combinacion funcione en los bordes.

Los subarboles se comparten entre varios arboles de la respuesta. LeetCode lo acepta porque solo lee los arboles, y evita copiar nodos de mas.

## Complejidad

- Tiempo: O(n * C_n), donde C_n es el numero de Catalan (la cantidad de arboles, 1430 para n = 8)
- Espacio: O(n * C_n) por la salida
