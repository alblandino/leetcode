# 69. Sqrt(x)

- **Dificultad:** Facil
- **Enlace:** https://leetcode.com/problems/sqrtx/

## Problema

Se recibe un entero no negativo `x` y hay que devolver su raiz cuadrada redondeada hacia abajo, es decir, el mayor entero `r` tal que `r * r <= x`.

No se permite usar funciones ni operadores de potencia, como `x ** 0.5` o `pow(x, 0.5)`.

## Ejemplos

```
Entrada: x = 4
Salida: 2
```

```
Entrada: x = 8
Salida: 2
```

La raiz de 8 es 2.82842..., que redondeada hacia abajo da 2.

## Restricciones

- `0 <= x <= 2^31 - 1`

## Solucion

Busqueda binaria sobre la respuesta. Si `r * r <= x`, cualquier numero menor que `r` tambien cumple; si `r * r > x`, cualquier numero mayor tampoco cumple. Por eso se puede buscar en el rango `[0, x]` partiendo a la mitad: si `mid * mid <= x`, `mid` es candidato y se busca a la derecha; si no, se busca a la izquierda.

Probar `r = 0, 1, 2, ...` hasta pasarse funciona, pero toma O(raiz de x) pasos. La busqueda binaria toma O(log x).

## Complejidad

- Tiempo: O(log x)
- Espacio: O(1)
