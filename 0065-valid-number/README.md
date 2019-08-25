# 65. Valid Number

- **Dificultad:** Dificil
- **Enlace:** https://leetcode.com/problems/valid-number/

## Problema

Se recibe una cadena `s` y hay que decir si representa un numero valido segun unas reglas fijas. Un numero valido es un entero o un decimal, seguido opcionalmente de un exponente.

- Entero: un signo opcional (`+` o `-`) y uno o mas digitos.
- Decimal: un signo opcional y luego digitos con punto al final (`4.`), digitos con punto en medio (`3.14`) o punto seguido de digitos (`.9`).
- Exponente: una `e` o `E` seguida de un entero (que puede tener signo, pero no punto).

Por ejemplo, son validos "2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93" y "-123.456e789". No son validos "abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3" y "95a54e53".

## Ejemplos

```
Entrada: s = "0"
Salida: true
```

```
Entrada: s = "e"
Salida: false
```

```
Entrada: s = "."
Salida: false
```

Un punto solo no tiene digitos ni antes ni despues.

## Restricciones

- `1 <= s.length <= 20`
- `s` solo contiene letras del alfabeto ingles (mayusculas y minusculas), digitos (`0-9`), mas `'+'`, menos `'-'` o punto `'.'`.

## Solucion

Se recorre la cadena una vez con tres banderas: si ya se vio algun digito en la parte actual, si ya se vio un punto y si ya se vio la `e`. Cada caracter se revisa con una regla simple:

- Digito: se marca que hay digitos.
- Signo: solo puede ir en la posicion 0 o justo despues de la `e`.
- Punto: no puede haber dos puntos, ni un punto despues de la `e`.
- `e` o `E`: no puede repetirse y antes debe haber al menos un digito. Despues de la `e` se reinicia la bandera de digitos, porque el exponente necesita sus propios digitos.
- Cualquier otro caracter hace que la cadena no sea valida.

Al final la cadena es valida solo si la ultima parte (la mantisa, o el exponente si lo hay) tiene al menos un digito. Una expresion regular tambien resuelve el problema, pero el recorrido deja cada regla a la vista.

## Complejidad

- Tiempo: O(n)
- Espacio: O(1)
