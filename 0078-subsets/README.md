# 78. Subsets

- **Dificultad:** Media
- **Enlace:** https://leetcode.com/problems/subsets/

## Problema

Se recibe un arreglo `nums` sin numeros repetidos y hay que devolver todos sus subconjuntos, incluido el vacio y el arreglo completo.

No puede haber subconjuntos repetidos, y tanto la lista como el orden de los subconjuntos dentro de ella pueden ser cualquiera.

## Ejemplos

```
Entrada: nums = [1,2,3]
Salida: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
```

```
Entrada: nums = [0]
Salida: [[],[0]]
```

## Restricciones

- `1 <= nums.length <= 10`
- `-10 <= nums[i] <= 10`
- Todos los numeros de `nums` son distintos.

## Solucion

Se construye la respuesta de forma iterativa. Se empieza con la lista que solo tiene el subconjunto vacio. Por cada numero de `nums`, cada subconjunto que ya existe genera uno nuevo igual pero con ese numero agregado, y los nuevos se suman a la lista.

Cada numero duplica la cantidad de subconjuntos, asi que al final hay 2^n, uno por cada forma de decidir si cada numero entra o no. Como los numeros son distintos, no se generan repetidos.

## Complejidad

- Tiempo: O(n * 2^n)
- Espacio: O(n * 2^n) por la salida
