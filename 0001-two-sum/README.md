# 1. Two Sum

- **Dificultad:** Facil
- **Enlace:** https://leetcode.com/problems/two-sum/

## Problema

Se recibe un arreglo de enteros `nums` y un entero `target`. Hay que devolver los indices de los dos numeros del arreglo que sumados dan `target`.

Siempre hay exactamente una respuesta, no se puede usar el mismo elemento dos veces y los indices se pueden devolver en cualquier orden.

## Ejemplos

```
Entrada: nums = [2,7,11,15], target = 9
Salida: [0,1]
```

```
Entrada: nums = [3,2,4], target = 6
Salida: [1,2]
```

```
Entrada: nums = [3,3], target = 6
Salida: [0,1]
```

## Restricciones

- `2 <= nums.length <= 10^4`
- `-10^9 <= nums[i] <= 10^9`
- `-10^9 <= target <= 10^9`
- Solo existe una respuesta valida.

## Solucion

Se recorre el arreglo una sola vez guardando en un diccionario cada numero con su indice. Antes de guardar un numero se revisa si su complemento (`target - num`) ya esta en el diccionario. Si esta, esos dos indices son la respuesta.

Con fuerza bruta (probar todas las parejas) seria O(n^2). El diccionario evita el segundo ciclo porque buscar en el es O(1).

## Complejidad

- Tiempo: O(n)
- Espacio: O(n)
