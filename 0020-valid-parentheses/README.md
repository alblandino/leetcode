# 20. Valid Parentheses

- **Dificultad:** Facil
- **Enlace:** https://leetcode.com/problems/valid-parentheses/

## Problema

Se recibe una cadena formada solo por los caracteres `(`, `)`, `{`, `}`, `[` y `]`, y hay que decir si esta bien balanceada.

Esta bien cuando cada simbolo que abre se cierra con uno de su mismo tipo, los cierres llegan en el orden correcto (lo ultimo que se abrio es lo primero que se cierra) y no sobra ningun cierre sin su apertura.

## Ejemplos

```
Entrada: s = "()[]{}"
Salida: true
```

```
Entrada: s = "(]"
Salida: false
```

El `(` se intenta cerrar con un `]`.

```
Entrada: s = "([)]"
Salida: false
```

El `)` llega cuando lo ultimo abierto es `[`, asi que el orden no es correcto.

## Restricciones

- `1 <= s.length <= 10^4`
- `s` contiene solo los caracteres `'()[]{}'`.

## Solucion

Se usa una pila. Cada simbolo que abre se apila. Cada simbolo que cierra debe coincidir con el que esta en la cima: si la pila esta vacia o el tope es de otro tipo, la cadena no es valida; si coincide, se saca de la pila.

Al terminar, la cadena es valida solo si la pila quedo vacia, porque cualquier cosa que quede es una apertura que nunca se cerro. Un diccionario de cierre a apertura evita escribir un `if` por cada tipo.

## Complejidad

- Tiempo: O(n)
- Espacio: O(n)
