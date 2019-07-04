# 49. Group Anagrams

- **Dificultad:** Media
- **Enlace:** https://leetcode.com/problems/group-anagrams/

## Problema

Se recibe una lista de palabras `strs`. Hay que juntar en grupos las que son anagramas entre si, es decir, las que tienen exactamente las mismas letras en la misma cantidad pero en otro orden.

Se devuelve la lista de grupos, y tanto los grupos como las palabras dentro de cada uno pueden ir en cualquier orden.

## Ejemplos

```
Entrada: strs = ["eat","tea","tan","ate","nat","bat"]
Salida: [["bat"],["nat","tan"],["ate","eat","tea"]]
```

"bat" no comparte letras con ninguna otra palabra, asi que queda sola.

```
Entrada: strs = [""]
Salida: [[""]]
```

```
Entrada: strs = ["a"]
Salida: [["a"]]
```

## Restricciones

- `1 <= strs.length <= 10^4`
- `0 <= strs[i].length <= 100`
- `strs[i]` solo tiene letras minusculas del alfabeto ingles.

## Solucion

Dos palabras son anagramas si al ordenar sus letras quedan iguales. Entonces se usa esa version ordenada como clave de un diccionario: se recorre la lista, se calcula la clave de cada palabra y se agrega la palabra a la lista de su clave. Al final los valores del diccionario son los grupos.

Comparar cada palabra contra todas las demas seria O(n^2 * k). Con el diccionario cada palabra se procesa una sola vez. Tambien se podria usar como clave un conteo de las 26 letras para evitar ordenar, pero con palabras de hasta 100 letras ordenar es sencillo y suficiente.

## Complejidad

- Tiempo: O(n * k log k), donde n es la cantidad de palabras y k el largo maximo de una palabra
- Espacio: O(n * k)
