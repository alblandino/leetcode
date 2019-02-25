# 8. String to Integer (atoi)

- **Dificultad:** Media
- **Enlace:** https://leetcode.com/problems/string-to-integer-atoi/

## Problema

Hay que implementar `myAtoi`, que convierte una cadena en un entero de 32 bits con signo leyendola de izquierda a derecha con estas reglas, en orden:

1. Se ignoran los espacios del inicio.
2. Si sigue un `'-'` o un `'+'`, define el signo (sin signo, el numero es positivo).
3. Se leen digitos hasta encontrar algo que no sea digito o hasta el final. Los ceros iniciales no cambian el valor. Si no se leyo ningun digito, el resultado es 0.
4. Si el numero queda fuera de `[-2^31, 2^31 - 1]`, se recorta al extremo mas cercano del rango.

No se puede usar ninguna funcion que convierta texto a numero (como `int()`), la conversion se hace a mano.

## Ejemplos

```
Entrada: s = " -042"
Salida: -42
```

Se salta el espacio, el `-` marca negativo y "042" vale 42.

```
Entrada: s = "1337c0d3"
Salida: 1337
```

La lectura se corta en la `c`.

```
Entrada: s = "words and 987"
Salida: 0
```

El primer caracter no es espacio, signo ni digito, asi que no se lee ningun numero.

## Restricciones

- `0 <= s.length <= 200`
- `s` contiene letras del alfabeto ingles (minusculas y mayusculas), digitos (`0 - 9`), `' '`, `'+'`, `'-'` y `'.'`.

## Solucion

Se recorre la cadena con un indice siguiendo los pasos tal cual: avanzar sobre los espacios, leer un signo opcional y luego acumular digitos con `result = result * 10 + digit`. El valor de cada digito se obtiene con `ord(char) - ord("0")`, sin usar `int()`.

El recorte al rango se revisa en cada digito y no solo al final: apenas el numero con signo pasa de `2^31 - 1` o baja de `-2^31`, se devuelve el limite. Asi el valor nunca crece mas de lo necesario aunque la cadena traiga muchos digitos.

## Complejidad

- Tiempo: O(n)
- Espacio: O(1)
