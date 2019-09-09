# 70. Climbing Stairs

- **Dificultad:** Facil
- **Enlace:** https://leetcode.com/problems/climbing-stairs/

## Problema

Una escalera tiene `n` escalones. En cada movimiento se puede subir 1 o 2 escalones. Hay que contar de cuantas formas distintas se puede llegar arriba.

## Ejemplos

```
Entrada: n = 2
Salida: 2
```

Se puede subir 1 + 1 o directamente 2.

```
Entrada: n = 3
Salida: 3
```

Las formas son 1 + 1 + 1, 1 + 2 y 2 + 1.

## Restricciones

- `1 <= n <= 45`

## Solucion

Al escalon `i` solo se llega desde el `i - 1` (con un paso de 1) o desde el `i - 2` (con un paso de 2). Entonces las formas de llegar a `i` son las formas de llegar a `i - 1` mas las de llegar a `i - 2`, la misma relacion que la serie de Fibonacci.

Como cada valor depende solo de los dos anteriores, basta con dos variables en lugar de una tabla completa. La recursion directa sin memo repite calculos y es exponencial.

## Complejidad

- Tiempo: O(n)
- Espacio: O(1)
