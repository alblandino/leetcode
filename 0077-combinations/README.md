# 77. Combinations

- **Dificultad:** Media
- **Enlace:** https://leetcode.com/problems/combinations/

## Problema

Dados dos enteros `n` y `k`, hay que listar todas las formas de elegir `k` numeros distintos entre 1 y `n`.

El orden dentro de una combinacion no importa: `[1,2]` y `[2,1]` son la misma y solo debe aparecer una vez. La lista final se puede devolver en cualquier orden.

## Ejemplos

```
Entrada: n = 4, k = 2
Salida: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
```

Hay 6 formas de elegir 2 numeros entre 4.

```
Entrada: n = 1, k = 1
Salida: [[1]]
```

## Restricciones

- `1 <= n <= 20`
- `1 <= k <= n`

## Solucion

Backtracking: se arma la combinacion de a un numero, siempre en orden creciente. Despues de poner un numero solo se prueban numeros mayores, asi cada combinacion se genera una sola vez y nunca aparece en otro orden. Cuando la combinacion llega a `k` numeros se guarda una copia y se deshace el ultimo paso para probar el siguiente.

Se agrega una poda simple: si desde el numero actual hasta `n` no quedan suficientes numeros para completar `k`, no vale la pena seguir por ese camino.

## Complejidad

- Tiempo: O(k * C(n, k)), donde C(n, k) es la cantidad de combinaciones
- Espacio: O(k) sin contar la salida (la combinacion actual y la recursion)
