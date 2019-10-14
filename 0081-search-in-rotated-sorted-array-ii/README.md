# 81. Search in Rotated Sorted Array II

- **Dificultad:** Media
- **Enlace:** https://leetcode.com/problems/search-in-rotated-sorted-array-ii/

## Problema

Se tiene un arreglo que estaba ordenado de menor a mayor (puede tener valores repetidos) y que despues fue rotado: se corto en algun punto y la parte del final se paso al inicio. Por ejemplo `[0,1,2,4,4,4,5,6,6,7]` puede quedar como `[4,5,6,6,7,0,1,2,4,4]`.

Hay que decir si `target` aparece en el arreglo, haciendo la menor cantidad de pasos posible (es decir, sin recorrerlo entero cuando se pueda evitar).

## Ejemplos

```
Entrada: nums = [2,5,6,0,0,1,2], target = 0
Salida: true
```

```
Entrada: nums = [2,5,6,0,0,1,2], target = 3
Salida: false
```

## Restricciones

- `1 <= nums.length <= 5000`
- `-10^4 <= nums[i] <= 10^4`
- Se garantiza que `nums` esta rotado en algun pivote.
- `-10^4 <= target <= 10^4`

## Solucion

Es una busqueda binaria adaptada. Al partir el rango en `mid`, al menos una de las dos mitades esta ordenada. Si la izquierda esta ordenada (`nums[left] <= nums[mid]`) se revisa si `target` cae dentro de sus limites; si cae se busca ahi, si no en la otra mitad. Lo mismo al reves cuando la ordenada es la derecha.

Los repetidos agregan un caso: si `nums[left]`, `nums[mid]` y `nums[right]` son iguales, no hay forma de saber cual mitad esta ordenada. En ese caso se descartan los dos extremos (ninguno es `target`, porque son iguales a `nums[mid]` y ya se reviso) y se sigue.

Respondiendo al follow up: los duplicados si afectan. En el peor caso (casi todos los valores iguales) solo se descarta un elemento por lado en cada paso y la busqueda se vuelve lineal.

## Complejidad

- Tiempo: O(log n) en el caso normal, O(n) en el peor caso con muchos repetidos
- Espacio: O(1)
