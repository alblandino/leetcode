# 10. Regular Expression Matching

- **Dificultad:** Dificil
- **Enlace:** https://leetcode.com/problems/regular-expression-matching/

## Problema

Se reciben una cadena `s` y un patron `p`, y hay que decir si el patron describe la cadena completa (no solo una parte). El patron tiene letras, que deben coincidir tal cual, y dos simbolos especiales:

- `.` coincide con cualquier caracter.
- `*` significa que el elemento justo anterior puede repetirse cero o mas veces.

## Ejemplos

```
Entrada: s = "aa", p = "a"
Salida: false
```

El patron solo cubre una `a`, falta la segunda.

```
Entrada: s = "aa", p = "a*"
Salida: true
```

`a*` repite la `a` dos veces.

```
Entrada: s = "ab", p = ".*"
Salida: true
```

`.*` es cualquier caracter repetido cualquier cantidad de veces.

## Restricciones

- `1 <= s.length <= 20`
- `1 <= p.length <= 20`
- `s` contiene solo letras minusculas del alfabeto ingles.
- `p` contiene solo letras minusculas del alfabeto ingles, `'.'` y `'*'`.
- Se garantiza que cada `'*'` tiene antes un caracter valido al que aplicarse.

## Solucion

Se usa programacion dinamica con una tabla `dp[i][j]` que dice si el sufijo `s[i:]` coincide con el sufijo `p[j:]`. El caso base es `dp[m][n] = True` (cadena vacia contra patron vacio) y la tabla se llena de atras hacia adelante.

Para cada celda se mira si el primer caracter coincide (`first_match`: hay caracter en `s` y es igual a `p[j]` o `p[j]` es `.`). Si el siguiente simbolo del patron es `*`, hay dos opciones: usar el elemento cero veces y saltar las dos posiciones del patron (`dp[i][j + 2]`), o, si el primer caracter coincide, consumirlo y quedarse en el mismo `x*` (`dp[i + 1][j]`). Si no hay `*`, el primer caracter debe coincidir y se avanza en ambos (`dp[i + 1][j + 1]`).

Una recursion sin memoria prueba las mismas combinaciones muchas veces y puede volverse exponencial con patrones como `a*a*a*`. La tabla resuelve cada par `(i, j)` una sola vez.

## Complejidad

- Tiempo: O(m * n)
- Espacio: O(m * n)
