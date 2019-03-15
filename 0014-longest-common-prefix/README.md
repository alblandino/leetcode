# 14. Longest Common Prefix

- **Dificultad:** Facil
- **Enlace:** https://leetcode.com/problems/longest-common-prefix/

## Problema

Se recibe una lista de palabras y hay que devolver el prefijo mas largo que todas tienen en comun, o sea, el tramo inicial que comparten.

Si no comparten ni la primera letra (o alguna palabra esta vacia), la respuesta es la cadena vacia `""`.

## Ejemplos

```
Entrada: strs = ["flower","flow","flight"]
Salida: "fl"
```

```
Entrada: strs = ["dog","racecar","car"]
Salida: ""
```

No hay ninguna letra inicial en comun.

## Restricciones

- `1 <= strs.length <= 200`
- `0 <= strs[i].length <= 200`
- `strs[i]` contiene solo letras minusculas del alfabeto ingles cuando no esta vacia.

## Solucion

Se toma la primera palabra como referencia y se revisa columna por columna: para cada posicion `i`, se compara su letra con la letra `i` de todas las demas palabras. Apenas una palabra se termina o tiene otra letra en esa posicion, el prefijo comun es `first[:i]`.

Si se recorre la primera palabra completa sin diferencias, ella misma es el prefijo. Revisar por columnas corta en cuanto aparece la primera diferencia, asi que no se leen letras de mas.

## Complejidad

- Tiempo: O(S), donde S es la cantidad total de letras
- Espacio: O(1) extra, sin contar la cadena que se devuelve
