# 86. Partition List

- **Dificultad:** Media
- **Enlace:** https://leetcode.com/problems/partition-list/

## Problema

Se recibe una lista enlazada y un valor `x`. Hay que reordenarla para que todos los nodos con valor menor que `x` queden antes que los nodos con valor mayor o igual a `x`.

Dentro de cada uno de los dos grupos se tiene que mantener el orden en que aparecian en la lista original. `x` no tiene por que estar en la lista.

## Ejemplos

```
Entrada: head = [1,4,3,2,5,2], x = 3
Salida: [1,2,2,4,3,5]
```

Los menores que 3 son `1,2,2` y los demas `4,3,5`, cada grupo en su orden original.

```
Entrada: head = [2,1], x = 2
Salida: [1,2]
```

## Restricciones

- El numero de nodos de la lista esta en el rango `[0, 200]`.
- `-100 <= Node.val <= 100`
- `-200 <= x <= 200`

## Solucion

Se arman dos listas por separado, cada una con su nodo ficticio: una para los nodos menores que `x` y otra para el resto. Se recorre la lista original una vez y cada nodo se engancha al final de la lista que le corresponde, asi el orden relativo se conserva solo.

Al final se une el final de la lista de menores con el inicio de la lista de mayores, y se pone `None` al final de la segunda para no dejar un ciclo con algun puntero viejo. No se crean nodos nuevos, solo se cambian enlaces.

## Complejidad

- Tiempo: O(n)
- Espacio: O(1)
