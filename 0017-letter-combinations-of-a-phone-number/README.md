# 17. Letter Combinations of a Phone Number

- **Dificultad:** Media
- **Enlace:** https://leetcode.com/problems/letter-combinations-of-a-phone-number/

## Problema

En el teclado de un telefono antiguo cada digito del 2 al 9 tiene asignadas algunas letras: 2 = abc, 3 = def, 4 = ghi, 5 = jkl, 6 = mno, 7 = pqrs, 8 = tuv y 9 = wxyz. El 1 no tiene letras.

Se recibe una cadena de digitos del 2 al 9 y hay que devolver todas las palabras que se pueden formar eligiendo una letra por cada digito, en el mismo orden. El orden de la lista no importa.

## Ejemplos

```
Entrada: digits = "23"
Salida: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
```

Se combina cada letra de "abc" con cada letra de "def".

```
Entrada: digits = "2"
Salida: ["a","b","c"]
```

## Restricciones

- `1 <= digits.length <= 4`
- `digits[i]` es un digito en el rango `['2', '9']`.

## Solucion

Se usa backtracking. Una funcion recursiva recibe la posicion del digito que toca y prueba cada una de sus letras: la agrega a la combinacion actual, se llama para el siguiente digito y despues la quita para probar la siguiente letra. Cuando la combinacion tiene tantas letras como digitos, se guarda.

Como hay que devolver todas las combinaciones, no se puede hacer mejor que generarlas una por una. Lo unico que se cuida es armar cada palabra sobre una sola lista que se reutiliza, en vez de crear cadenas nuevas en cada nivel.

## Complejidad

- Tiempo: O(4^n * n), con hasta 4 letras por digito y n letras por palabra
- Espacio: O(n) para la recursion, sin contar la salida
