# 41. First Missing Positive

- **Dificultad:** Dificil
- **Enlace:** https://leetcode.com/problems/first-missing-positive/

## Problema

Se recibe un arreglo `nums` desordenado que puede tener negativos, ceros y repetidos. Hay que devolver el entero positivo mas pequeno que no aparece en el arreglo.

La solucion debe correr en O(n) y usar solo memoria extra constante.

## Ejemplos

```
Entrada: nums = [1,2,0]
Salida: 3
```

```
Entrada: nums = [3,4,-1,1]
Salida: 2
```

El 1 esta, pero el 2 no.

```
Entrada: nums = [7,8,9,11,12]
Salida: 1
```

## Restricciones

- `1 <= nums.length <= 10^5`
- `-2^31 <= nums[i] <= 2^31 - 1`

## Solucion

Si el arreglo tiene `n` elementos, la respuesta esta entre 1 y `n + 1`, asi que solo importan los valores de 1 a `n`. La idea es usar el mismo arreglo como tabla: cada valor `v` en ese rango se intercambia hasta dejarlo en la posicion `v - 1`. Los valores fuera de rango o repetidos se quedan donde caigan. Despues se recorre el arreglo y la primera posicion `i` que no tiene el valor `i + 1` indica que falta `i + 1`. Si todas estan bien, la respuesta es `n + 1`.

Ordenar seria O(n log n) y un set seria O(n) de memoria extra; ninguno cumple lo que pide el problema. Cada intercambio deja un valor en su lugar definitivo, por eso el total de intercambios es como mucho `n` y todo queda en O(n).

## Complejidad

- Tiempo: O(n)
- Espacio: O(1), se modifica el arreglo de entrada
