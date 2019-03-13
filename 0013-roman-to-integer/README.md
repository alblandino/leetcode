# 13. Roman to Integer

- **Dificultad:** Facil
- **Enlace:** https://leetcode.com/problems/roman-to-integer/

## Problema

Se recibe un numero romano valido (entre 1 y 3999) y hay que devolver su valor entero. Los simbolos son `I` = 1, `V` = 5, `X` = 10, `L` = 50, `C` = 100, `D` = 500 y `M` = 1000.

Normalmente los simbolos van de mayor a menor y se suman, como `XXVII` = 27. La excepcion son seis casos donde un simbolo menor va antes de uno mayor y se resta: `IV` (4), `IX` (9), `XL` (40), `XC` (90), `CD` (400) y `CM` (900).

## Ejemplos

```
Entrada: s = "III"
Salida: 3
```

```
Entrada: s = "LVIII"
Salida: 58
```

L = 50, V = 5 y III = 3.

```
Entrada: s = "MCMXCIV"
Salida: 1994
```

M = 1000, CM = 900, XC = 90 y IV = 4.

## Restricciones

- `1 <= s.length <= 15`
- `s` contiene solo los caracteres `('I', 'V', 'X', 'L', 'C', 'D', 'M')`.
- Se garantiza que `s` es un numero romano valido en el rango `[1, 3999]`.

## Solucion

Se recorre la cadena de izquierda a derecha con un diccionario de valores. Si un simbolo vale menos que el que tiene a su derecha, es parte de una resta y su valor se descuenta; si no, se suma.

Por ejemplo en `IX` la `I` resta 1 y la `X` suma 10, lo que da 9. Asi no hace falta buscar los seis pares especiales por separado, la comparacion con el vecino ya los detecta.

## Complejidad

- Tiempo: O(n)
- Espacio: O(1)
