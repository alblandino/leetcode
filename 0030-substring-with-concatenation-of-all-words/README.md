# 30. Substring with Concatenation of All Words

- **Dificultad:** Dificil
- **Enlace:** https://leetcode.com/problems/substring-with-concatenation-of-all-words/

## Problema

Se recibe una cadena `s` y una lista `words` donde todas las palabras tienen el mismo largo. Hay que encontrar cada posicion de `s` donde empieza un pedazo formado por todas las palabras de `words` pegadas una detras de otra, en cualquier orden, usando cada palabra exactamente las veces que aparece en la lista.

Se devuelven los indices de inicio de esos pedazos, en cualquier orden.

## Ejemplos

```
Entrada: s = "barfoothefoobarman", words = ["foo","bar"]
Salida: [0,9]
```

En 0 empieza "barfoo" y en 9 empieza "foobar".

```
Entrada: s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]
Salida: []
```

```
Entrada: s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]
Salida: [6,9,12]
```

## Restricciones

- `1 <= s.length <= 10^4`
- `1 <= words.length <= 5000`
- `1 <= words[i].length <= 30`
- `s` y `words[i]` solo tienen letras minusculas del alfabeto ingles.

## Solucion

Sea `L` el largo de cada palabra. Cualquier respuesta empieza en una posicion cuyo resto al dividir entre `L` es 0, 1, ..., `L - 1`, asi que se hace una pasada por cada uno de esos desplazamientos, leyendo `s` de palabra en palabra. En cada pasada se mantiene una ventana deslizante con un contador de las palabras que tiene dentro. Si la palabra leida no esta en `words`, la ventana se vacia y empieza despues de ella. Si la palabra aparece mas veces de las permitidas, se sacan palabras por la izquierda hasta que vuelva a estar en el limite. Cuando la ventana tiene tantas palabras como `words`, su inicio es una respuesta.

La fuerza bruta revisaria cada indice de `s` armando un contador nuevo cada vez, lo que repite casi todo el trabajo. Con la ventana cada palabra de `s` entra y sale como maximo una vez por pasada.

## Complejidad

- Tiempo: O(n * L + m * L), donde n es el largo de `s`, m la cantidad de palabras y L el largo de cada una
- Espacio: O(m * L) por los contadores de palabras
