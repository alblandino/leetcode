# 66. Plus One

- **Dificultad:** Facil
- **Enlace:** https://leetcode.com/problems/plus-one/

## Problema

Un numero entero grande viene guardado como una lista de digitos, del mas significativo al menos significativo, y sin ceros a la izquierda. Hay que sumarle 1 y devolver el resultado con el mismo formato de lista de digitos.

## Ejemplos

```
Entrada: digits = [1,2,3]
Salida: [1,2,4]
```

```
Entrada: digits = [4,3,2,1]
Salida: [4,3,2,2]
```

```
Entrada: digits = [9]
Salida: [1,0]
```

9 + 1 = 10, asi que la lista crece un digito.

## Restricciones

- `1 <= digits.length <= 100`
- `0 <= digits[i] <= 9`
- `digits` no tiene ceros a la izquierda.

## Solucion

Se hace la suma como a mano, desde el ultimo digito. Si el digito es menor que 9, se le suma 1 y se termina. Si es 9, se vuelve 0 y el acarreo pasa al digito de la izquierda. Si todos los digitos eran 9, al final queda una lista de ceros y se le agrega un 1 adelante.

Convertir la lista a entero, sumar y volver a separar tambien funciona en Python, pero la idea del problema es manejar el acarreo sin depender de enteros grandes.

## Complejidad

- Tiempo: O(n)
- Espacio: O(n) por la copia de la lista (O(1) extra si se modificara la entrada)
