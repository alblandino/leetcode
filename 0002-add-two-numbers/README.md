# 2. Add Two Numbers

- **Dificultad:** Media
- **Enlace:** https://leetcode.com/problems/add-two-numbers/

## Problema

Se reciben dos listas enlazadas no vacias. Cada una representa un numero entero no negativo, guardando un digito por nodo y con los digitos al reves: el primer nodo es la unidad, el segundo la decena, y asi sucesivamente.

Hay que sumar los dos numeros y devolver el resultado como una lista enlazada con el mismo formato (digitos al reves). Los numeros no tienen ceros a la izquierda, salvo el propio 0.

## Ejemplos

```
Entrada: l1 = [2,4,3], l2 = [5,6,4]
Salida: [7,0,8]
```

Las listas representan 342 y 465, y 342 + 465 = 807.

```
Entrada: l1 = [0], l2 = [0]
Salida: [0]
```

```
Entrada: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Salida: [8,9,9,9,0,0,0,1]
```

## Restricciones

- La cantidad de nodos de cada lista esta en el rango `[1, 100]`.
- `0 <= Node.val <= 9`
- Se garantiza que la lista representa un numero sin ceros a la izquierda.

## Solucion

Como los digitos vienen desde la unidad, se puede sumar igual que a mano: se recorren las dos listas al mismo tiempo, se suman los digitos de la misma posicion mas el acarreo, se guarda `total % 10` en un nodo nuevo y el acarreo pasa a ser `total // 10`.

El ciclo sigue mientras quede algun nodo en cualquiera de las listas o un acarreo pendiente, asi se cubren listas de distinto largo y el digito extra del final (por ejemplo 5 + 5 = 10). Un nodo ficticio al inicio evita tratar aparte el primer nodo del resultado.

Convertir las listas a enteros y sumarlos no sirve en general: con 100 digitos el numero no cabe en un entero de 64 bits en la mayoria de los lenguajes.

## Complejidad

- Tiempo: O(max(m, n))
- Espacio: O(max(m, n)) por la lista resultado
