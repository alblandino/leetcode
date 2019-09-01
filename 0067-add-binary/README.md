# 67. Add Binary

- **Dificultad:** Facil
- **Enlace:** https://leetcode.com/problems/add-binary/

## Problema

Se reciben dos numeros escritos en binario como cadenas de `'0'` y `'1'`. Hay que sumarlos y devolver el resultado tambien como cadena binaria.

Las cadenas pueden tener largos distintos y pueden ser muy largas (hasta 10^4 digitos).

## Ejemplos

```
Entrada: a = "11", b = "1"
Salida: "100"
```

```
Entrada: a = "1010", b = "1011"
Salida: "10101"
```

## Restricciones

- `1 <= a.length, b.length <= 10^4`
- `a` y `b` solo tienen caracteres `'0'` o `'1'`.
- Ninguna cadena tiene ceros a la izquierda, salvo el propio cero.

## Solucion

Suma columna por columna como a mano, desde el final de las dos cadenas hacia el inicio. En cada paso se suman los dos digitos (o 0 si una cadena ya se acabo) y el acarreo. El digito del resultado es `total % 2` y el nuevo acarreo es `total // 2`. El ciclo sigue mientras quede algun digito o acarreo.

Los digitos se van guardando en una lista en orden inverso y al final se da vuelta y se une. Convertir con `int(a, 2)` resolveria el problema en una linea, pero se salta justamente lo que el ejercicio quiere practicar.

## Complejidad

- Tiempo: O(max(n, m))
- Espacio: O(max(n, m)) para el resultado
