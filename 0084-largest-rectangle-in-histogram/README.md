# 84. Largest Rectangle in Histogram

- **Dificultad:** Dificil
- **Enlace:** https://leetcode.com/problems/largest-rectangle-in-histogram/

## Problema

Se recibe una lista `heights` que representa un histograma: cada barra mide 1 de ancho y tiene la altura indicada. Hay que encontrar el area del rectangulo mas grande que se puede dibujar dentro del histograma.

El rectangulo tiene que estar formado por barras consecutivas y su altura queda limitada por la barra mas baja de ese tramo.

## Ejemplos

```
Entrada: heights = [2,1,5,6,2,3]
Salida: 10
```

El mejor rectangulo usa las barras de altura 5 y 6, con altura 5 y ancho 2.

```
Entrada: heights = [2,4]
Salida: 4
```

## Restricciones

- `1 <= heights.length <= 10^5`
- `0 <= heights[i] <= 10^4`

## Solucion

Para cada barra, el mejor rectangulo que la usa como la mas baja se extiende hacia los lados hasta encontrar una barra mas baja. Una pila monotona permite encontrar esos limites en una sola pasada: la pila guarda indices con alturas crecientes.

Cuando llega una barra mas baja que la del tope, la barra del tope ya no puede extenderse mas a la derecha. Se saca de la pila y su rectangulo va desde justo despues del nuevo tope (su limite izquierdo) hasta la barra anterior a la actual. Al final se agrega una barra imaginaria de altura 0 para vaciar la pila.

La fuerza bruta (probar cada par de extremos) es O(n^2) y no alcanza para 10^5 barras.

## Complejidad

- Tiempo: O(n), cada indice entra y sale de la pila una vez
- Espacio: O(n)
