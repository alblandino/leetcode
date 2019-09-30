# 76. Minimum Window Substring

- **Dificultad:** Dificil
- **Enlace:** https://leetcode.com/problems/minimum-window-substring/

## Problema

Se tienen dos cadenas, `s` y `t`. Hay que encontrar el pedazo continuo mas corto de `s` que contenga todas las letras de `t`, contando las repeticiones: si `t` tiene dos `a`, la ventana tambien necesita al menos dos `a`.

Si ningun pedazo de `s` cumple, se devuelve la cadena vacia. Mayusculas y minusculas cuentan como letras distintas, y los casos de prueba garantizan que la respuesta es unica.

## Ejemplos

```
Entrada: s = "ADOBECODEBANC", t = "ABC"
Salida: "BANC"
```

```
Entrada: s = "a", t = "a"
Salida: "a"
```

```
Entrada: s = "a", t = "aa"
Salida: ""
```

`t` pide dos `a` y `s` solo tiene una, asi que no existe una ventana valida.

## Restricciones

- `m == s.length`
- `n == t.length`
- `1 <= m, n <= 10^5`
- `s` y `t` solo tienen letras del alfabeto ingles, mayusculas y minusculas.

## Solucion

Se usa una ventana deslizante con dos punteros. Un diccionario guarda cuantas veces le falta cada letra de `t` a la ventana y un contador `missing` dice cuantas letras faltan en total. El puntero derecho avanza metiendo letras en la ventana; cada vez que una letra cubre algo que faltaba, `missing` baja.

Cuando `missing` llega a 0 la ventana ya contiene todo `t`. En ese momento se guarda si es la mas corta vista hasta ahora y se mueve el puntero izquierdo para achicarla, hasta que vuelva a faltar alguna letra. Cada caracter entra y sale de la ventana una sola vez.

Revisar todas las subcadenas una por una seria O(m^2) o peor, demasiado lento para 10^5 caracteres.

## Complejidad

- Tiempo: O(m + n)
- Espacio: O(1), el diccionario tiene a lo sumo 52 letras distintas
