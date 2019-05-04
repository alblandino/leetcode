# 29. Divide Two Integers

- **Dificultad:** Media
- **Enlace:** https://leetcode.com/problems/divide-two-integers/

## Problema

Se reciben dos enteros, `dividend` y `divisor`, y hay que devolver el cociente de la division entera sin usar multiplicacion, division ni modulo. El resultado se trunca hacia cero: se descarta la parte decimal, tanto para positivos como para negativos.

Se asume que solo se pueden guardar enteros de 32 bits con signo. Si el cociente pasa de `2^31 - 1`, se devuelve `2^31 - 1`; si queda por debajo de `-2^31`, se devuelve `-2^31`.

## Ejemplos

```
Entrada: dividend = 10, divisor = 3
Salida: 3
```

```
Entrada: dividend = 7, divisor = -3
Salida: -2
```

7 / -3 da -2.33..., y al quitar los decimales queda -2.

## Restricciones

- `-2^31 <= dividend, divisor <= 2^31 - 1`
- `divisor != 0`

## Solucion

Se trabaja con los valores absolutos y el signo se decide al final (es negativo si solo uno de los dos lo es). Restar el divisor una vez por vuelta seria demasiado lento si el dividendo es grande y el divisor es 1, asi que se resta en bloques: se duplica el divisor sumandolo consigo mismo (`chunk + chunk`) mientras siga cabiendo en lo que queda, y a la vez se duplica el contador de cuantas veces representa ese bloque. Se resta el bloque mas grande, se suma su contador al cociente y se repite con el resto.

El unico caso que se sale del rango de 32 bits es `-2^31 / -1`, que daria `2^31`; se revisa al inicio y se devuelve `2^31 - 1`. No se usan desplazamientos de bits, solo sumas, restas y comparaciones.

## Complejidad

- Tiempo: O(log^2 n), donde n es el valor absoluto de `dividend` (cada bloque se arma en O(log n) y hay O(log n) bloques)
- Espacio: O(1)
