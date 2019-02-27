# 9. Palindrome Number

- **Dificultad:** Facil
- **Enlace:** https://leetcode.com/problems/palindrome-number/

## Problema

Se recibe un entero `x` y hay que decir si es palindromo, es decir, si sus digitos se leen igual de izquierda a derecha que de derecha a izquierda.

Los negativos nunca lo son, porque el signo `-` solo queda de un lado. Como reto extra, el enunciado propone resolverlo sin convertir el numero a texto.

## Ejemplos

```
Entrada: x = 121
Salida: true
```

```
Entrada: x = -121
Salida: false
```

Al reves se leeria "121-".

```
Entrada: x = 10
Salida: false
```

Al reves se leeria "01".

## Restricciones

- `-2^31 <= x <= 2^31 - 1`

## Solucion

Se resuelve sin texto invirtiendo solo la mitad derecha del numero. Se sacan digitos del final de `x` con `% 10` y se van armando en `reversed_half`, hasta que `reversed_half` alcanza o pasa a lo que queda de `x`. En ese punto ya se proceso la mitad de los digitos.

Si el numero tiene cantidad par de digitos, las dos mitades deben ser iguales. Si es impar, el digito del medio quedo al final de `reversed_half` y se descarta con `// 10`. Antes se descartan los negativos y los numeros que terminan en 0 (salvo el 0), porque ninguno puede ser palindromo y romperian la condicion del ciclo.

Invertir el numero completo tambien sirve, pero invertir solo la mitad evita cualquier riesgo de desbordamiento en lenguajes con enteros de 32 bits.

## Complejidad

- Tiempo: O(log x), uno por digito
- Espacio: O(1)
