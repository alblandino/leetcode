# 42. Trapping Rain Water

- **Dificultad:** Dificil
- **Enlace:** https://leetcode.com/problems/trapping-rain-water/

## Problema

Se recibe un arreglo `height` con las alturas de una fila de barras, todas de ancho 1. Despues de llover, el agua se queda atrapada en los huecos entre barras altas. Hay que calcular cuantas unidades de agua quedan atrapadas en total.

## Ejemplos

```
Entrada: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Salida: 6
```

```
Entrada: height = [4,2,0,3,2,5]
Salida: 9
```

## Restricciones

- `n == height.length`
- `1 <= n <= 2 * 10^4`
- `0 <= height[i] <= 10^5`

## Solucion

Sobre cada barra queda `min(maximo a la izquierda, maximo a la derecha) - altura` de agua. Se usan dos punteros, uno en cada extremo, y se guardan el maximo visto desde la izquierda y el maximo visto desde la derecha. En cada paso se mueve el puntero del lado con la barra mas baja: ese lado tiene garantizado un muro igual o mas alto al otro extremo, asi que su agua solo depende de su propio maximo. Se suma `maximo - altura` y se avanza.

Calcular los dos maximos para cada barra recorriendo hacia los lados seria O(n^2). Tambien se pueden guardar en dos arreglos de prefijos en O(n), pero los dos punteros evitan esa memoria extra.

## Complejidad

- Tiempo: O(n)
- Espacio: O(1)
