# 6. Zigzag Conversion

- **Dificultad:** Media
- **Enlace:** https://leetcode.com/problems/zigzag-conversion/

## Problema

Se recibe una cadena `s` y un numero de filas `numRows`. Los caracteres se acomodan en zigzag: el primero va en la fila de arriba, los siguientes bajan una fila cada uno hasta llegar a la ultima, luego suben en diagonal hasta la primera, y asi se repite. Con "PAYPALISHIRING" y 3 filas queda:

```
P   A   H   N
A P L S I I G
Y   I   R
```

Hay que devolver la cadena que resulta de leer ese dibujo fila por fila, de arriba hacia abajo.

## Ejemplos

```
Entrada: s = "PAYPALISHIRING", numRows = 3
Salida: "PAHNAPLSIIGYIR"
```

```
Entrada: s = "PAYPALISHIRING", numRows = 4
Salida: "PINALSIGYAHRPI"
```

Con 4 filas, P, A, Y, P bajan por la primera columna, A y L suben en diagonal y la I vuelve a quedar en la fila de arriba.

```
Entrada: s = "A", numRows = 1
Salida: "A"
```

## Restricciones

- `1 <= s.length <= 1000`
- `s` contiene letras del alfabeto ingles (minusculas y mayusculas), `','` y `'.'`.
- `1 <= numRows <= 1000`

## Solucion

No hace falta armar el dibujo completo con espacios. Basta con una cadena por fila y saber en que fila va cada caracter. Se recorre `s` con un indice de fila y una direccion: se baja (+1) hasta la ultima fila y ahi se cambia a subir (-1) hasta la primera. Cada caracter se agrega a la fila actual.

Al final se concatenan las filas en orden. Si hay una sola fila, o mas filas que caracteres, el resultado es la misma cadena, y se devuelve directo para no tener que cambiar la direccion en una fila que es a la vez la primera y la ultima.

## Complejidad

- Tiempo: O(n)
- Espacio: O(n)
