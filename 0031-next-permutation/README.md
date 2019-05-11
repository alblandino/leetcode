# 31. Next Permutation

- **Dificultad:** Media
- **Enlace:** https://leetcode.com/problems/next-permutation/

## Problema

Se recibe un arreglo de enteros `nums`. Si se ordenaran todas las formas de acomodar sus elementos como en un diccionario, hay que transformar `nums` en la que sigue justo despues de la actual.

Si `nums` ya es la ultima (todo en orden descendente), se pasa a la primera, que es el arreglo en orden ascendente. El cambio se hace dentro del mismo arreglo y con memoria extra constante.

## Ejemplos

```
Entrada: nums = [1,2,3]
Salida: [1,3,2]
```

```
Entrada: nums = [3,2,1]
Salida: [1,2,3]
```

No hay una mayor que [3,2,1], asi que se vuelve a la menor.

```
Entrada: nums = [1,1,5]
Salida: [1,5,1]
```

## Restricciones

- `1 <= nums.length <= 100`
- `0 <= nums[i] <= 100`

## Solucion

Desde la derecha se busca el primer indice `i` donde `nums[i] < nums[i + 1]`. Todo lo que esta a la derecha de `i` va en orden descendente, o sea que ya es la mayor combinacion posible de esa parte; para avanzar hay que cambiar `nums[i]`. Se busca, otra vez desde la derecha, el primer elemento mayor que `nums[i]` y se intercambian. Despues la parte derecha sigue en orden descendente, y se invierte para dejarla en su forma mas pequena.

Si no existe ese `i`, el arreglo completo esta en orden descendente y basta con invertirlo entero. Generar todas las permutaciones y buscar la siguiente seria O(n!), asi que se descarta.

## Complejidad

- Tiempo: O(n)
- Espacio: O(1)
