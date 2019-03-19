# 15. 3Sum

- **Dificultad:** Media
- **Enlace:** https://leetcode.com/problems/3sum/

## Problema

Se recibe un arreglo de enteros `nums` y hay que encontrar todos los grupos de tres numeros, tomados de posiciones distintas, que sumen 0.

La respuesta no puede tener grupos repetidos: dos tripletas con los mismos valores cuentan como una sola, aunque salgan de posiciones distintas. El orden de las tripletas y de los numeros dentro de cada una no importa.

## Ejemplos

```
Entrada: nums = [-1,0,1,2,-1,-4]
Salida: [[-1,-1,2],[-1,0,1]]
```

Hay dos formas de armar [-1,0,1] con los indices, pero se devuelve una sola vez.

```
Entrada: nums = [0,1,1]
Salida: []
```

```
Entrada: nums = [0,0,0]
Salida: [[0,0,0]]
```

## Restricciones

- `3 <= nums.length <= 3000`
- `-10^5 <= nums[i] <= 10^5`

## Solucion

Primero se ordena el arreglo. Luego se fija el primer numero `nums[i]` y se buscan los otros dos con dos punteros en el resto: `left` justo despues de `i` y `right` al final. Si la suma es menor que 0 se avanza `left` para subirla, si es mayor se retrocede `right` para bajarla, y si da 0 se guarda la tripleta y se mueven ambos.

El orden tambien sirve para evitar duplicados: se salta un `nums[i]` igual al anterior, y despues de encontrar una tripleta se avanza `left` mientras repita el mismo valor. Ademas, si `nums[i]` ya es positivo se puede cortar, porque los que siguen son mayores y no pueden sumar 0.

Probar todas las tripletas seria O(n^3) y obligaria a usar un conjunto para quitar repetidos.

## Complejidad

- Tiempo: O(n^2)
- Espacio: O(n) por la copia ordenada, sin contar la salida
