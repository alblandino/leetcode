# 89. Gray Code

- **Dificultad:** Media
- **Enlace:** https://leetcode.com/problems/gray-code/

## Problema

Dado `n`, hay que devolver una secuencia con todos los numeros de 0 a 2^n - 1, cada uno una sola vez, empezando en 0. La condicion es que dos numeros seguidos en la secuencia, vistos en binario, se diferencien en exactamente un bit.

La secuencia es circular: el ultimo y el primero tambien deben diferir en un solo bit. Si hay varias respuestas validas, cualquiera sirve.

## Ejemplos

```
Entrada: n = 2
Salida: [0,1,3,2]
```

En binario es `00, 01, 11, 10`: cada paso cambia un solo bit, y de `10` a `00` tambien. `[0,2,3,1]` tambien seria valida.

```
Entrada: n = 1
Salida: [0,1]
```

## Restricciones

- `1 <= n <= 16`

## Solucion

Se construye por reflexion. Se empieza con la secuencia de 0 bits, que es solo `[0]`. Para pasar de `k` a `k + 1` bits se toma la secuencia actual, se copia en orden inverso y a cada numero de la copia se le suma `2^k` (es decir, se le prende el bit nuevo). La secuencia nueva es la original seguida de la copia.

Funciona porque dentro de cada mitad los vecinos ya difieren en un bit. En la union, el ultimo de la original y el primero de la copia son el mismo numero, uno con el bit nuevo y otro sin el. Y el final de la copia es el 0 inicial con el bit nuevo, asi que tambien cierra el circulo con el 0.

## Complejidad

- Tiempo: O(2^n)
- Espacio: O(2^n) por la salida
