# 3. Longest Substring Without Repeating Characters

- **Dificultad:** Media
- **Enlace:** https://leetcode.com/problems/longest-substring-without-repeating-characters/

## Problema

Dada una cadena `s`, hay que encontrar el largo del tramo continuo mas largo en el que ningun caracter se repite.

Importa que sea continuo: un conjunto de letras tomadas salteadas no cuenta. Si la cadena esta vacia, la respuesta es 0.

## Ejemplos

```
Entrada: s = "abcabcbb"
Salida: 3
```

El tramo "abc" tiene 3 caracteres distintos.

```
Entrada: s = "bbbbb"
Salida: 1
```

```
Entrada: s = "pwwkew"
Salida: 3
```

El tramo es "wke". "pwke" no vale porque no es continuo dentro de la cadena.

## Restricciones

- `0 <= s.length <= 10^5`
- `s` contiene letras del alfabeto ingles, digitos, simbolos y espacios.

## Solucion

Se usa una ventana deslizante `[start, i]` que nunca tiene caracteres repetidos, y un diccionario con la ultima posicion donde se vio cada caracter.

Al llegar a un caracter que ya aparecio dentro de la ventana, el inicio salta justo despues de esa aparicion anterior. Si la aparicion anterior quedo antes de `start`, no se toca nada (por eso se compara con `start`, como en "abba"). En cada paso se actualiza el mejor largo con el tamano de la ventana.

Revisar todos los tramos posibles seria O(n^2) o peor. Con la ventana cada caracter se procesa una sola vez.

## Complejidad

- Tiempo: O(n)
- Espacio: O(k), donde k es la cantidad de caracteres distintos
