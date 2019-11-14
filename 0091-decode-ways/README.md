# 91. Decode Ways

- **Dificultad:** Media
- **Enlace:** https://leetcode.com/problems/decode-ways/

## Problema

Un mensaje de letras se codifico como numeros con `A = 1`, `B = 2`, ..., `Z = 26`, y los numeros quedaron pegados en una sola cadena de digitos `s`. Hay que contar de cuantas formas distintas se puede volver a separar la cadena en letras.

Cada pedazo debe ser un numero de 1 a 26 escrito sin ceros a la izquierda: `"6"` es valido, pero `"06"` no. Si la cadena no se puede decodificar de ninguna forma, la respuesta es 0.

## Ejemplos

```
Entrada: s = "12"
Salida: 2
```

Puede ser `1 2` (AB) o `12` (L).

```
Entrada: s = "226"
Salida: 3
```

Puede ser `2 26`, `22 6` o `2 2 6`.

```
Entrada: s = "06"
Salida: 0
```

El cero inicial no se puede leer solo ni como parte de `"06"`.

## Restricciones

- `1 <= s.length <= 100`
- `s` solo contiene digitos y puede tener ceros al inicio.

## Solucion

Programacion dinamica. `dp[i]` es la cantidad de formas de decodificar los primeros `i` digitos, con `dp[0] = 1` (la cadena vacia tiene una forma: no hacer nada).

Para calcular `dp[i]` se miran las dos maneras de terminar: tomando el ultimo digito solo, que vale si no es `0`, y entonces se suma `dp[i - 1]`; o tomando los dos ultimos digitos juntos, que vale si forman un numero entre 10 y 26, y entonces se suma `dp[i - 2]`. Pedir que este entre 10 y 26 descarta los pares que empiezan en 0.

Probar todas las separaciones con recursion sin memoria seria exponencial, porque los mismos sufijos se recalculan muchas veces.

## Complejidad

- Tiempo: O(n)
- Espacio: O(n)
