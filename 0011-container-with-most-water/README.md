# 11. Container With Most Water

- **Dificultad:** Media
- **Enlace:** https://leetcode.com/problems/container-with-most-water/

## Problema

Se recibe un arreglo `height` donde cada valor es la altura de una linea vertical, y las lineas estan separadas por una unidad. Hay que elegir dos lineas que, junto con el piso, formen un recipiente.

La cantidad de agua que guarda es el ancho (distancia entre las dos lineas) por la altura de la linea mas baja, porque el agua se derrama por el lado mas corto. Hay que devolver la mayor cantidad de agua posible.

## Ejemplos

```
Entrada: height = [1,8,6,2,5,4,8,3,7]
Salida: 49
```

Las lineas de altura 8 (posicion 1) y 7 (posicion 8) dan 7 de ancho por 7 de alto.

```
Entrada: height = [1,1]
Salida: 1
```

## Restricciones

- `n == height.length`
- `2 <= n <= 10^5`
- `0 <= height[i] <= 10^4`

## Solucion

Se usan dos punteros, uno en cada extremo, que empiezan con el ancho maximo. En cada paso se calcula el area actual, se guarda si es la mejor, y se mueve hacia adentro el puntero de la linea mas baja.

Mover la linea mas alta nunca ayuda: el ancho baja y la altura sigue limitada por la mas baja, asi que el area no puede crecer. La unica forma de mejorar es cambiar la linea baja por otra que quiza sea mas alta. Por eso se descartan esos pares sin revisarlos.

Probar todos los pares de lineas seria O(n^2), demasiado lento con `n` hasta `10^5`.

## Complejidad

- Tiempo: O(n)
- Espacio: O(1)
