# 87. Scramble String

- **Dificultad:** Dificil
- **Enlace:** https://leetcode.com/problems/scramble-string/

## Problema

Una cadena se "revuelve" asi: si tiene una sola letra, queda igual. Si tiene mas, se corta en dos partes no vacias en cualquier punto, se decide si intercambiarlas o dejarlas en su lugar, y se repite lo mismo dentro de cada parte.

Dadas dos cadenas `s1` y `s2` del mismo largo, hay que decir si `s2` se puede obtener revolviendo `s1` de esta forma.

## Ejemplos

```
Entrada: s1 = "great", s2 = "rgeat"
Salida: true
```

Se corta en `gr | eat`, luego `gr` en `g | r` y se intercambia a `rg`; el resto queda igual.

```
Entrada: s1 = "abcde", s2 = "caebd"
Salida: false
```

```
Entrada: s1 = "a", s2 = "a"
Salida: true
```

## Restricciones

- `s1.length == s2.length`
- `1 <= s1.length <= 30`
- `s1` y `s2` solo tienen letras minusculas del alfabeto ingles.

## Solucion

Se define `check(i, j, length)`: si el pedazo de `s1` que empieza en `i` se puede revolver para obtener el pedazo de `s2` que empieza en `j`, ambos de largo `length`. Si los pedazos son iguales la respuesta es si; si no tienen las mismas letras es no.

En otro caso se prueba cada punto de corte `k`. Sin intercambio, la primera parte de `s1` debe corresponder a la primera parte de `s2` y la segunda con la segunda. Con intercambio, la primera parte de `s1` (largo `k`) debe corresponder al final de `s2` y la segunda parte al inicio. Basta que un corte funcione.

Sin memoria la recursion es exponencial porque los mismos pedazos se revisan muchas veces. Por eso se guarda cada resultado en un diccionario con la llave `(i, j, length)`, y hay a lo sumo n^3 llaves distintas.

## Complejidad

- Tiempo: O(n^4), n^3 estados y n cortes por estado
- Espacio: O(n^3) por el diccionario de memoria
