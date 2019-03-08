# 12. Integer to Roman

- **Dificultad:** Media
- **Enlace:** https://leetcode.com/problems/integer-to-roman/

## Problema

Se recibe un entero entre 1 y 3999 y hay que escribirlo en numeros romanos. Los simbolos son `I` = 1, `V` = 5, `X` = 10, `L` = 50, `C` = 100, `D` = 500 y `M` = 1000.

El numero se arma de la cifra mas grande a la mas chica, sumando simbolos. `I`, `X`, `C` y `M` se pueden repetir hasta 3 veces seguidas; `V`, `L` y `D` no se repiten. Para los 4 y los 9 se usa la forma de resta, que pone un simbolo menor antes de uno mayor, y solo existen seis: `IV` (4), `IX` (9), `XL` (40), `XC` (90), `CD` (400) y `CM` (900).

## Ejemplos

```
Entrada: num = 3749
Salida: "MMMDCCXLIX"
```

3000 = MMM, 700 = DCC, 40 = XL y 9 = IX.

```
Entrada: num = 58
Salida: "LVIII"
```

```
Entrada: num = 1994
Salida: "MCMXCIV"
```

1000 = M, 900 = CM, 90 = XC y 4 = IV.

## Restricciones

- `1 <= num <= 3999`

## Solucion

Se arma una lista con los 13 valores posibles ordenados de mayor a menor, incluyendo las seis formas de resta como si fueran simbolos propios (`CM`, `CD`, `XC`, etc). Luego se aplica un metodo goloso: mientras el valor actual quepa en lo que queda del numero, se agrega su simbolo y se resta.

Al tratar 900, 400, 90, 40, 9 y 4 como simbolos aparte, las reglas de la resta se cumplen solas y no hace falta revisar cada cifra con casos especiales.

## Complejidad

- Tiempo: O(1), el numero esta acotado a 3999 y hay 13 simbolos
- Espacio: O(1)
