# 72. Edit Distance

- **Dificultad:** Media
- **Enlace:** https://leetcode.com/problems/edit-distance/

## Problema

Se reciben dos palabras, `word1` y `word2`. Hay que calcular el menor numero de operaciones para transformar `word1` en `word2`, donde cada operacion es insertar un caracter, borrar un caracter o reemplazar un caracter por otro.

Este valor se conoce como distancia de edicion o distancia de Levenshtein.

## Ejemplos

```
Entrada: word1 = "horse", word2 = "ros"
Salida: 3
```

Se reemplaza la `h` por `r` (rorse), se borra la segunda `r` (rose) y se borra la `e` (ros).

```
Entrada: word1 = "intention", word2 = "execution"
Salida: 5
```

## Restricciones

- `0 <= word1.length, word2.length <= 500`
- `word1` y `word2` solo tienen letras minusculas del alfabeto ingles.

## Solucion

Programacion dinamica. `dp[i][j]` es la distancia entre los primeros `i` caracteres de `word1` y los primeros `j` de `word2`. Los bordes son faciles: pasar de `i` caracteres a una cadena vacia cuesta `i` borrados, y de vacia a `j` caracteres cuesta `j` inserciones.

Para el resto, si `word1[i - 1] == word2[j - 1]` el ultimo caracter ya coincide y `dp[i][j] = dp[i - 1][j - 1]`. Si no, se toma la mejor de tres opciones mas 1: reemplazar (`dp[i - 1][j - 1]`), borrar de `word1` (`dp[i - 1][j]`) o insertar en `word1` (`dp[i][j - 1]`). La respuesta queda en `dp[m][n]`. Probar todas las secuencias de operaciones con recursion simple seria exponencial.

## Complejidad

- Tiempo: O(m * n)
- Espacio: O(m * n)
