# 43. Multiply Strings

- **Dificultad:** Media
- **Enlace:** https://leetcode.com/problems/multiply-strings/

## Problema

Se reciben dos numeros no negativos escritos como cadenas, `num1` y `num2`, y hay que devolver su producto tambien como cadena.

No se vale convertir las cadenas completas a entero ni usar una libreria de numeros grandes: la multiplicacion se tiene que hacer digito por digito.

## Ejemplos

```
Entrada: num1 = "2", num2 = "3"
Salida: "6"
```

```
Entrada: num1 = "123", num2 = "456"
Salida: "56088"
```

## Restricciones

- `1 <= num1.length, num2.length <= 200`
- `num1` y `num2` solo tienen digitos.
- Ninguno de los dos tiene ceros a la izquierda, salvo el propio numero 0.

## Solucion

Es la multiplicacion de la escuela. El producto tiene como maximo `len(num1) + len(num2)` digitos, asi que se crea un arreglo de ese tamano con ceros. Al multiplicar el digito `i` de `num1` por el digito `j` de `num2` (contando desde la izquierda), el resultado cae en las posiciones `i + j` (decenas) e `i + j + 1` (unidades). Se recorren los dos numeros de derecha a izquierda, se suma cada producto en `i + j + 1` y el acarreo se pasa a `i + j`.

Al final se quitan los ceros a la izquierda y se arma la cadena. El caso en que alguno es `"0"` se responde al inicio. Cada caracter se pasa a digito con `ord(c) - ord("0")`, sin convertir el numero entero.

## Complejidad

- Tiempo: O(m * n), donde m y n son los largos de `num1` y `num2`
- Espacio: O(m + n)
