# 50. Pow(x, n)

- **Dificultad:** Media
- **Enlace:** https://leetcode.com/problems/powx-n/

## Problema

Hay que implementar la potencia: dado un numero real `x` y un entero `n` (que puede ser negativo), devolver `x` elevado a `n`.

Un exponente negativo significa dividir: `x^-n = 1 / x^n`.

## Ejemplos

```
Entrada: x = 2.00000, n = 10
Salida: 1024.00000
```

```
Entrada: x = 2.10000, n = 3
Salida: 9.26100
```

```
Entrada: x = 2.00000, n = -2
Salida: 0.25000
```

2^-2 es 1 / 2^2, o sea 1/4.

## Restricciones

- `-100.0 < x < 100.0`
- `-2^31 <= n <= 2^31-1`
- `n` es un entero.
- `x` no es cero o `n > 0`.
- `-10^4 <= x^n <= 10^4`

## Solucion

Si `n` es negativo, se cambia `x` por `1 / x` y `n` por `-n`, y el problema queda con exponente positivo. Luego se usa exponenciacion rapida: mientras `n > 0`, si `n` es impar se multiplica el resultado por `x`; despues `x` se eleva al cuadrado y `n` se divide entre 2. Funciona porque `x^n = (x^2)^(n/2)` cuando `n` es par, y cuando es impar sobra un `x` que se acumula en el resultado.

Multiplicar `x` por si mismo `n` veces seria O(n), y con `n` cerca de 2^31 es demasiado lento. Partiendo el exponente a la mitad en cada paso solo hacen falta unas 31 vueltas.

## Complejidad

- Tiempo: O(log n)
- Espacio: O(1)
