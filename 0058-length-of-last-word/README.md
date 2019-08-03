# 58. Length of Last Word

- **Dificultad:** Facil
- **Enlace:** https://leetcode.com/problems/length-of-last-word/

## Problema

Se recibe una cadena `s` formada por palabras separadas por espacios. Puede haber varios espacios seguidos, y tambien espacios al inicio o al final.

Hay que devolver cuantas letras tiene la ultima palabra. Una palabra es un bloque de caracteres sin espacios.

## Ejemplos

```
Entrada: s = "Hello World"
Salida: 5
```

```
Entrada: s = "   fly me   to   the moon  "
Salida: 4
```

La ultima palabra es "moon"; los espacios del final no cuentan.

```
Entrada: s = "luffy is still joyboy"
Salida: 6
```

## Restricciones

- `1 <= s.length <= 10^4`
- `s` solo contiene letras del alfabeto ingles y espacios `' '`.
- Hay al menos una palabra en `s`.

## Solucion

Se recorre la cadena desde el final. Primero se saltan los espacios del final y despues se cuentan caracteres hasta encontrar un espacio o llegar al inicio. Ese conteo es el largo de la ultima palabra.

Usar `split()` y tomar el ultimo elemento tambien sirve, pero arma una lista con todas las palabras. Recorrer desde atras solo mira lo necesario y no usa memoria extra.

## Complejidad

- Tiempo: O(n)
- Espacio: O(1)
