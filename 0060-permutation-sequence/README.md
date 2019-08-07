# 60. Permutation Sequence

- **Dificultad:** Dificil
- **Enlace:** https://leetcode.com/problems/permutation-sequence/

## Problema

Con los numeros del 1 al `n` se pueden formar `n!` permutaciones. Si se escriben todas como cadenas y se ordenan de menor a mayor (para `n = 3`: "123", "132", "213", "231", "312", "321"), hay que devolver la que ocupa el lugar `k` de esa lista, contando desde 1.

## Ejemplos

```
Entrada: n = 3, k = 3
Salida: "213"
```

```
Entrada: n = 4, k = 9
Salida: "2314"
```

```
Entrada: n = 3, k = 1
Salida: "123"
```

## Restricciones

- `1 <= n <= 9`
- `1 <= k <= n!`

## Solucion

No hace falta generar las permutaciones. Las permutaciones que empiezan con el mismo numero forman bloques de `(n - 1)!` elementos. Con `k` contado desde 0, el primer digito es el que esta en la posicion `k // (n - 1)!` de la lista de numeros disponibles. Se quita ese numero, se queda `k` como `k % (n - 1)!` y se repite con los numeros que quedan y bloques de `(n - 2)!`, y asi hasta usar todos.

Generar las permutaciones en orden hasta llegar a la `k` cuesta O(n! * n), que con `n = 9` son cientos de miles de cadenas. Este metodo solo hace `n` pasos.

## Complejidad

- Tiempo: O(n^2), porque quitar un elemento de la lista de disponibles es O(n)
- Espacio: O(n)
