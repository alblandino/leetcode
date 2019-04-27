# 27. Remove Element

- **Dificultad:** Facil
- **Enlace:** https://leetcode.com/problems/remove-element/

## Problema

Se recibe un arreglo `nums` y un valor `val`. Hay que quitar todas las apariciones de `val` dentro del mismo arreglo y devolver `k`, la cantidad de elementos que no son `val`.

Las primeras `k` posiciones de `nums` deben quedar con esos elementos, en cualquier orden. Lo que quede despues de la posicion `k - 1` no se revisa.

## Ejemplos

```
Entrada: nums = [3,2,2,3], val = 3
Salida: 2, nums = [2,2,_,_]
```

```
Entrada: nums = [0,1,2,2,3,0,4,2], val = 2
Salida: 5, nums = [0,1,4,0,3,_,_,_]
```

Los cinco primeros valores pueden venir en otro orden; el `_` marca posiciones que no importan.

## Restricciones

- `0 <= nums.length <= 100`
- `0 <= nums[i] <= 50`
- `0 <= val <= 100`

## Solucion

Se recorre el arreglo con un indice `i` y se lleva otro indice `k` que apunta a donde va el siguiente elemento que se queda. Cada vez que `nums[i]` es distinto de `val`, se copia en `nums[k]` y `k` avanza. Al terminar, las primeras `k` posiciones tienen justo los elementos validos.

Como `k` nunca pasa a `i`, nunca se pisa un valor que todavia no se leyo. No hace falta un arreglo auxiliar.

## Complejidad

- Tiempo: O(n)
- Espacio: O(1)
