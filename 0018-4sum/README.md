# 18. 4Sum

- **Dificultad:** Media
- **Enlace:** https://leetcode.com/problems/4sum/

## Problema

Se recibe un arreglo de enteros `nums` y un entero `target`. Hay que devolver todos los grupos de cuatro numeros, tomados de cuatro posiciones distintas, que sumen exactamente `target`.

No puede haber grupos repetidos (mismos valores aunque vengan de otras posiciones) y el orden de la respuesta no importa.

## Ejemplos

```
Entrada: nums = [1,0,-1,0,-2,2], target = 0
Salida: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
```

```
Entrada: nums = [2,2,2,2,2], target = 8
Salida: [[2,2,2,2]]
```

Hay cinco 2, pero el grupo [2,2,2,2] se cuenta una sola vez.

## Restricciones

- `1 <= nums.length <= 200`
- `-10^9 <= nums[i] <= 10^9`
- `-10^9 <= target <= 10^9`

## Solucion

Es 3Sum con un nivel mas. Se ordena el arreglo, se fijan los dos primeros numeros con dos ciclos (`a` y `b`) y los otros dos se buscan con dos punteros sobre el resto: si la suma es menor que `target` se avanza `left`, si es mayor se retrocede `right`, y si es igual se guarda el grupo.

Para no repetir grupos se saltan los valores iguales al anterior en `a`, en `b` y en `left` despues de cada acierto. En Python la suma de cuatro numeros de hasta `10^9` no desborda; en lenguajes con enteros de 32 bits habria que sumar en 64 bits.

Probar todas las cuaternas seria O(n^4). Los dos punteros reemplazan los dos ciclos internos por una sola pasada.

## Complejidad

- Tiempo: O(n^3)
- Espacio: O(n) por la copia ordenada, sin contar la salida
