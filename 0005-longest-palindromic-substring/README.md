# 5. Longest Palindromic Substring

- **Dificultad:** Media
- **Enlace:** https://leetcode.com/problems/longest-palindromic-substring/

## Problema

Dada una cadena `s`, hay que devolver el tramo continuo mas largo que sea palindromo, es decir, que se lea igual de izquierda a derecha que de derecha a izquierda.

Si hay varios tramos con el largo maximo, cualquiera de ellos es una respuesta valida.

## Ejemplos

```
Entrada: s = "babad"
Salida: "bab"
```

"aba" tambien es correcta.

```
Entrada: s = "cbbd"
Salida: "bb"
```

## Restricciones

- `1 <= s.length <= 1000`
- `s` contiene solo digitos y letras del alfabeto ingles.

## Solucion

Todo palindromo tiene un centro: un caracter (largo impar, como "aba") o el espacio entre dos caracteres (largo par, como "bb"). Se prueba cada uno de los `2n - 1` centros y se expande hacia los lados mientras los caracteres de ambos extremos sean iguales. Se guarda el inicio y el largo del mejor palindromo encontrado.

Revisar todos los tramos y comprobar si cada uno es palindromo seria O(n^3). Expandir desde el centro baja a O(n^2) sin memoria extra, lo que alcanza de sobra para `n <= 1000`. Existe el algoritmo de Manacher en O(n), pero es mucho mas dificil de escribir y no hace falta aqui.

## Complejidad

- Tiempo: O(n^2)
- Espacio: O(1)
