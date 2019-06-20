# 44. Wildcard Matching

- **Dificultad:** Dificil
- **Enlace:** https://leetcode.com/problems/wildcard-matching/

## Problema

Se recibe un texto `s` y un patron `p`. El patron tiene letras normales y dos comodines: `'?'` vale por exactamente un caracter cualquiera, y `'*'` vale por cualquier secuencia de caracteres, incluso vacia.

Hay que decir si el patron cubre el texto completo, no solo una parte.

## Ejemplos

```
Entrada: s = "aa", p = "a"
Salida: false
```

El patron solo cubre una de las dos letras.

```
Entrada: s = "aa", p = "*"
Salida: true
```

```
Entrada: s = "cb", p = "?a"
Salida: false
```

El `'?'` cubre la `c`, pero la `a` no coincide con la `b`.

## Restricciones

- `0 <= s.length, p.length <= 2000`
- `s` solo tiene letras minusculas del alfabeto ingles.
- `p` solo tiene letras minusculas del alfabeto ingles, `'?'` o `'*'`.

## Solucion

Se usa programacion dinamica con una tabla `dp` donde `dp[i][j]` dice si los primeros `i` caracteres de `s` encajan con los primeros `j` del patron. `dp[0][0]` es verdadero (vacio con vacio), y con el texto vacio solo encaja un patron formado por `'*'`. Para el resto: si `p[j - 1]` es letra o `'?'`, se necesita que coincida con `s[i - 1]` y que `dp[i - 1][j - 1]` sea verdadero. Si es `'*'`, hay dos opciones: que no cubra nada (`dp[i][j - 1]`) o que cubra un caracter mas de `s` (`dp[i - 1][j]`).

Una recursion directa probaria todas las formas de repartir el texto entre los `'*'` y puede volverse exponencial. La tabla guarda cada subproblema una sola vez.

## Complejidad

- Tiempo: O(m * n), donde m es el largo de `s` y n el de `p`
- Espacio: O(m * n)
