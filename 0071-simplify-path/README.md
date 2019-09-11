# 71. Simplify Path

- **Dificultad:** Media
- **Enlace:** https://leetcode.com/problems/simplify-path/

## Problema

Se recibe una ruta absoluta de un sistema de archivos tipo Unix (siempre empieza con `/`) y hay que devolverla en su forma canonica, es decir, la version mas limpia que apunta al mismo lugar.

En la entrada, `.` significa la carpeta actual, `..` significa subir a la carpeta padre y varias barras seguidas valen como una sola. Cualquier otro nombre, incluso `...` o `....`, es un nombre normal de carpeta.

La ruta canonica empieza con una sola `/`, separa las carpetas con una sola `/`, no termina en `/` (salvo que sea la raiz) y no contiene `.` ni `..`.

## Ejemplos

```
Entrada: path = "/home//foo/"
Salida: "/home/foo"
```

La barra doble se vuelve una sola y la barra del final se quita.

```
Entrada: path = "/home/user/Documents/../Pictures"
Salida: "/home/user/Pictures"
```

```
Entrada: path = "/.../a/../b/c/../d/./"
Salida: "/.../b/d"
```

`...` es un nombre de carpeta valido.

## Restricciones

- `1 <= path.length <= 3000`
- `path` solo tiene letras del alfabeto ingles, digitos, punto `'.'`, barra `'/'` o `'_'`.
- `path` es una ruta absoluta de Unix valida.

## Solucion

Se separa la ruta por `/` y se usa una pila con las carpetas del camino actual. Las partes vacias (que salen de barras repetidas o de la barra inicial y final) y los `.` se ignoran. Un `..` saca la ultima carpeta de la pila, si hay alguna, porque desde la raiz no se puede subir. Cualquier otro nombre se agrega a la pila.

Al final la ruta canonica es `/` seguida de las carpetas de la pila unidas con `/`. Si la pila queda vacia, el resultado es solo `/`.

## Complejidad

- Tiempo: O(n)
- Espacio: O(n)
