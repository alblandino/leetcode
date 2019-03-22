# 16. 3Sum Closest

- **Dificultad:** Media
- **Enlace:** https://leetcode.com/problems/3sum-closest/

## Problema

Se recibe un arreglo de enteros `nums` y un entero `target`. Hay que elegir tres numeros de posiciones distintas cuya suma quede lo mas cerca posible de `target`, y devolver esa suma (no los numeros).

Se puede asumir que hay una sola suma que es la mas cercana.

## Ejemplos

```
Entrada: nums = [-1,2,1,-4], target = 1
Salida: 2
```

-1 + 2 + 1 = 2 es la suma que menos se aleja de 1.

```
Entrada: nums = [0,0,0], target = 1
Salida: 0
```

## Restricciones

- `3 <= nums.length <= 500`
- `-1000 <= nums[i] <= 1000`
- `-10^4 <= target <= 10^4`

## Solucion

Es la misma idea que 3Sum: se ordena el arreglo, se fija el primer numero y los otros dos se buscan con dos punteros. En cada paso se calcula la suma y, si esta mas cerca de `target` que la mejor guardada, se reemplaza.

Si la suma es menor que `target` se avanza `left` para subirla; si es mayor se retrocede `right` para bajarla. Si es igual, no se puede estar mas cerca y se devuelve de inmediato.

Probar todas las tripletas seria O(n^3). Con los dos punteros cada numero fijo se resuelve en una sola pasada.

## Complejidad

- Tiempo: O(n^2)
- Espacio: O(n) por la copia ordenada
