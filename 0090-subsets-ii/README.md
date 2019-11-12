# 90. Subsets II

- **Dificultad:** Media
- **Enlace:** https://leetcode.com/problems/subsets-ii/

## Problema

Igual que el problema 78, hay que devolver todos los subconjuntos de `nums`, pero ahora el arreglo puede tener numeros repetidos.

Dos subconjuntos con los mismos valores cuentan como el mismo, asi que cada uno debe aparecer una sola vez en la respuesta. El orden de la lista no importa.

## Ejemplos

```
Entrada: nums = [1,2,2]
Salida: [[],[1],[1,2],[1,2,2],[2],[2,2]]
```

`[1,2]` aparece una sola vez aunque hay dos 2 distintos para elegir.

```
Entrada: nums = [0]
Salida: [[],[0]]
```

## Restricciones

- `1 <= nums.length <= 10`
- `-10 <= nums[i] <= 10`

## Solucion

Primero se ordena el arreglo para que los valores iguales queden juntos. Despues se usa backtracking: cada llamada guarda el subconjunto actual y prueba agregar cada numero a partir de una posicion `start`.

La clave para no repetir es que, dentro de un mismo nivel de la recursion, si un numero es igual al anterior se salta. Elegir el segundo 2 en ese nivel generaria exactamente los mismos subconjuntos que ya genero el primero. En niveles mas profundos si se permite usarlo, y asi se forman `[2,2]`.

Generar todo y quitar repetidos con un set tambien funciona, pero hace trabajo de mas y necesita convertir cada subconjunto a tupla.

## Complejidad

- Tiempo: O(n * 2^n)
- Espacio: O(n) sin contar la salida
