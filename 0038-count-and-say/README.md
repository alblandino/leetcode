# 38. Count and Say

- **Dificultad:** Media
- **Enlace:** https://leetcode.com/problems/count-and-say/

## Problema

La secuencia "contar y decir" empieza con `"1"`, y cada termino nuevo se obtiene leyendo en voz alta el anterior: se agrupan los digitos iguales que estan seguidos y cada grupo se escribe como "cuantos hay" seguido de "que digito es".

Por ejemplo, `"3322251"` tiene los grupos `33`, `222`, `5` y `1`, asi que se escribe `"23" + "32" + "15" + "11" = "23321511"`. Dado `n`, hay que devolver el termino numero `n` de la secuencia.

## Ejemplos

```
Entrada: n = 4
Salida: "1211"
```

Los terminos son "1", "11" (un 1), "21" (dos 1) y "1211" (un 2, un 1).

```
Entrada: n = 1
Salida: "1"
```

## Restricciones

- `1 <= n <= 30`

## Solucion

Se arranca con `"1"` y se aplica `n - 1` veces una funcion que codifica la cadena actual. Esa funcion recorre la cadena con dos indices: `i` marca el inicio de un grupo y `j` avanza mientras el digito sea el mismo. El grupo se escribe como `str(j - i) + digito` y se sigue desde `j`. Los pedazos se juntan en una lista y se unen al final para no crear muchas cadenas intermedias.

Se hace de forma iterativa, como pide el seguimiento del problema; la version recursiva hace lo mismo pero gasta pila sin necesidad.

## Complejidad

- Tiempo: O(n * L), donde L es el largo del termino mas largo (crece aproximadamente un 30% en cada paso)
- Espacio: O(L)
