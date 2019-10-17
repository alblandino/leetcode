# 82. Remove Duplicates from Sorted List II

- **Dificultad:** Media
- **Enlace:** https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/

## Problema

Se recibe la cabeza de una lista enlazada ordenada. Si un valor aparece mas de una vez, hay que borrar todos los nodos con ese valor, no solo las copias extra. Solo quedan los valores que aparecian una unica vez.

La lista resultante sigue ordenada y se devuelve su nueva cabeza, que puede cambiar o quedar vacia.

## Ejemplos

```
Entrada: head = [1,2,3,3,4,4,5]
Salida: [1,2,5]
```

```
Entrada: head = [1,1,1,2,3]
Salida: [2,3]
```

Aqui se borra la cabeza original, porque el 1 estaba repetido.

## Restricciones

- El numero de nodos de la lista esta en el rango `[0, 300]`.
- `-100 <= Node.val <= 100`
- Se garantiza que la lista esta ordenada de forma ascendente.

## Solucion

Se usa un nodo ficticio (`dummy`) antes de la cabeza, para que borrar el primer nodo no sea un caso especial. El puntero `prev` apunta siempre al ultimo nodo que seguro se queda.

Al recorrer, si el nodo actual tiene el mismo valor que el siguiente, se avanza hasta pasar todo el bloque con ese valor y se conecta `prev` directamente con el primer nodo distinto. Si el nodo no esta repetido, `prev` avanza hasta el. Como la lista esta ordenada, los repetidos siempre estan juntos.

## Complejidad

- Tiempo: O(n)
- Espacio: O(1)
