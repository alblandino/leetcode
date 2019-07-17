# 53. Maximum Subarray

- **Dificultad:** Media
- **Enlace:** https://leetcode.com/problems/maximum-subarray/

## Problema

Se recibe un arreglo de enteros `nums` (puede tener negativos). Hay que encontrar el tramo continuo del arreglo cuya suma sea la mayor posible y devolver esa suma.

El tramo debe tener al menos un elemento, asi que si todos los numeros son negativos la respuesta es el mayor de ellos.

## Ejemplos

```
Entrada: nums = [-2,1,-3,4,-1,2,1,-5,4]
Salida: 6
```

El tramo `[4,-1,2,1]` suma 6.

```
Entrada: nums = [1]
Salida: 1
```

```
Entrada: nums = [5,4,-1,7,8]
Salida: 23
```

Aqui conviene tomar el arreglo completo.

## Restricciones

- `1 <= nums.length <= 10^5`
- `-10^4 <= nums[i] <= 10^4`

## Solucion

Algoritmo de Kadane. Se recorre el arreglo llevando la mejor suma de un tramo que termina en la posicion actual. Para cada numero hay dos opciones: sumarlo al tramo que venia o empezar un tramo nuevo desde el. Se empieza de nuevo cuando la suma acumulada ya es negativa, porque solo restaria. En cada paso se actualiza el maximo global.

La fuerza bruta revisa todos los pares inicio/fin y es O(n^2). LeetCode sugiere tambien divide y venceras, que es O(n log n); Kadane es mas simple y mas rapido.

## Complejidad

- Tiempo: O(n)
- Espacio: O(1)
