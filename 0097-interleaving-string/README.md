# 97. Interleaving String

- **Dificultad:** Media
- **Enlace:** https://leetcode.com/problems/interleaving-string/

## Problema

Se tienen tres cadenas `s1`, `s2` y `s3`. Hay que decir si `s3` se puede formar mezclando las letras de `s1` y `s2`, tomando pedazos de una y de otra de forma alternada pero sin cambiar el orden de las letras dentro de cada una.

Dicho de otra forma: hay que repartir las letras de `s3` entre `s1` y `s2` de modo que, leidas en orden, las de un lado formen exactamente `s1` y las del otro exactamente `s2`.

## Ejemplos

```
Entrada: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Salida: true
```

Se puede armar como `"aa" + "dbbc" + "bc" + "a" + "c"`, alternando pedazos de `s1` y `s2`.

```
Entrada: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
Salida: false
```

```
Entrada: s1 = "", s2 = "", s3 = ""
Salida: true
```

## Restricciones

- `0 <= s1.length, s2.length <= 100`
- `0 <= s3.length <= 200`
- `s1`, `s2` y `s3` solo tienen letras minusculas del alfabeto ingles.

## Solucion

Si los largos no suman, la respuesta es `false` de inmediato. Si suman, se usa programacion dinamica: `dp[i][j]` dice si los primeros `i + j` caracteres de `s3` se pueden formar con los primeros `i` de `s1` y los primeros `j` de `s2`.

El ultimo caracter de ese prefijo de `s3` tuvo que salir de `s1` o de `s2`. Si sale de `s1`, debe ser igual a `s1[i - 1]` y `dp[i - 1][j]` debe ser verdadero; si sale de `s2`, igual con `s2[j - 1]` y `dp[i][j - 1]`. El caso base es `dp[0][0] = true` y la respuesta es `dp[len(s1)][len(s2)]`.

Un intento greedy (tomar de la cadena que coincida) falla cuando las dos coinciden, y probar ambas ramas sin memoria es exponencial. La tabla se podria reducir a una sola fila de largo `len(s2) + 1` para el follow up, pero la tabla completa es mas facil de leer.

## Complejidad

- Tiempo: O(m * n), con m y n los largos de `s1` y `s2`
- Espacio: O(m * n)
