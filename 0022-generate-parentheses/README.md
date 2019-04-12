# 22. Generate Parentheses

- **Dificultad:** Media
- **Enlace:** https://leetcode.com/problems/generate-parentheses/

## Problema

Se recibe un numero `n` y hay que devolver todas las cadenas distintas que se pueden formar con `n` parentesis que abren y `n` que cierran, de modo que queden bien balanceadas (cada `(` tiene su `)` y nunca se cierra algo que no se abrio).

## Ejemplos

```
Entrada: n = 3
Salida: ["((()))","(()())","(())()","()(())","()()()"]
```

```
Entrada: n = 1
Salida: ["()"]
```

## Restricciones

- `1 <= n <= 8`

## Solucion

Se arma cada cadena caracter por caracter con backtracking, llevando la cuenta de cuantos `(` y `)` se usaron. Solo se agrega un `(` si todavia quedan (`open_count < n`), y solo se agrega un `)` si hay alguno abierto sin cerrar (`close_count < open_count`). Cuando la cadena llega a largo `2n` se guarda.

Con esas dos reglas nunca se construye una cadena invalida, asi que no hay que revisarlas al final. Generar las `2^(2n)` cadenas posibles y filtrar las balanceadas tambien funciona, pero hace mucho trabajo de mas.

## Complejidad

- Tiempo: O(4^n / sqrt(n)), que es del orden de la cantidad de respuestas validas
- Espacio: O(n) para la recursion, sin contar la salida
