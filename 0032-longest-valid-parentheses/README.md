# 32. Longest Valid Parentheses

- **Dificultad:** Dificil
- **Enlace:** https://leetcode.com/problems/longest-valid-parentheses/

## Problema

Se recibe una cadena que solo tiene `'('` y `')'`. Hay que devolver el largo del pedazo continuo mas largo donde los parentesis estan bien balanceados, es decir, cada `'('` se cierra con un `')'` en el orden correcto.

Si no hay ningun pedazo valido, la respuesta es 0.

## Ejemplos

```
Entrada: s = "(()"
Salida: 2
```

El pedazo valido mas largo es "()".

```
Entrada: s = ")()())"
Salida: 4
```

El pedazo valido mas largo es "()()".

```
Entrada: s = ""
Salida: 0
```

## Restricciones

- `0 <= s.length <= 3 * 10^4`
- `s[i]` es `'('` o `')'`.

## Solucion

Se usa una pila de indices. En el fondo de la pila siempre queda el indice justo antes del tramo valido actual (al inicio es `-1`). Cada `'('` mete su indice. Cada `')'` saca el tope: si la pila queda vacia, ese `')'` no tenia pareja y su indice pasa a ser el nuevo fondo; si no queda vacia, el tramo valido que termina en `i` mide `i - pila[-1]` y se compara con el mejor.

Revisar todos los pedazos posibles y validar cada uno seria O(n^3), o O(n^2) con algo de cuidado. La pila resuelve todo en una sola pasada.

## Complejidad

- Tiempo: O(n)
- Espacio: O(n)
