# 28. Find the Index of the First Occurrence in a String

- **Dificultad:** Facil
- **Enlace:** https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/

## Problema

Se reciben dos cadenas, `haystack` (el texto) y `needle` (lo que se busca). Hay que devolver el indice donde empieza la primera aparicion de `needle` dentro de `haystack`.

Si `needle` no aparece en ninguna parte, se devuelve `-1`.

## Ejemplos

```
Entrada: haystack = "sadbutsad", needle = "sad"
Salida: 0
```

"sad" aparece en los indices 0 y 6; se devuelve el primero.

```
Entrada: haystack = "leetcode", needle = "leeto"
Salida: -1
```

## Restricciones

- `1 <= haystack.length, needle.length <= 10^4`
- `haystack` y `needle` solo tienen letras minusculas del alfabeto ingles.

## Solucion

Se prueba cada posicion inicial `i` donde todavia cabe `needle` (de `0` a `n - m`) y se compara el pedazo `haystack[i:i + m]` con `needle`. La primera posicion donde coinciden es la respuesta. Si ninguna coincide, se devuelve `-1`.

Existe el algoritmo KMP que lo hace en O(n + m) usando una tabla de prefijos, pero es mas largo de escribir. Con estos limites la comparacion directa es suficiente y es la que se espera en un problema facil.

## Complejidad

- Tiempo: O((n - m + 1) * m), donde n es el largo de `haystack` y m el de `needle`
- Espacio: O(m) por el pedazo que se compara en cada paso
