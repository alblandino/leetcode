# 100. Same Tree

- **Dificultad:** Facil
- **Enlace:** https://leetcode.com/problems/same-tree/

## Problema

Se reciben las raices de dos arboles binarios, `p` y `q`, y hay que decir si son el mismo arbol.

Son el mismo si tienen exactamente la misma forma y cada nodo de uno tiene el mismo valor que el nodo en la misma posicion del otro. Cualquiera de los dos puede estar vacio.

## Ejemplos

```
Entrada: p = [1,2,3], q = [1,2,3]
Salida: true
```

```
Entrada: p = [1,2], q = [1,null,2]
Salida: false
```

Tienen los mismos valores, pero el 2 es hijo izquierdo en uno y derecho en el otro.

```
Entrada: p = [1,2,1], q = [1,1,2]
Salida: false
```

## Restricciones

- El numero de nodos en ambos arboles esta en el rango `[0, 100]`.
- `-10^4 <= Node.val <= 10^4`

## Solucion

Se comparan los dos arboles a la vez de forma recursiva. Si los dos nodos son `None`, coinciden. Si solo uno es `None`, o si sus valores son distintos, no son iguales. En otro caso, son iguales solo si sus subarboles izquierdos son iguales y sus subarboles derechos tambien.

Con a lo sumo 100 nodos la recursion no tiene problemas de profundidad. Comparar los recorridos de los dos arboles tambien funciona, pero solo si se incluyen los huecos; la recursion directa es mas simple y se detiene en la primera diferencia.

## Complejidad

- Tiempo: O(n), con n el numero de nodos del arbol mas chico
- Espacio: O(h) por la recursion, con h la altura del arbol
