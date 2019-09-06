# 68. Text Justification

- **Dificultad:** Dificil
- **Enlace:** https://leetcode.com/problems/text-justification/

## Problema

Se recibe una lista de palabras y un ancho `maxWidth`. Hay que acomodar las palabras en lineas de exactamente `maxWidth` caracteres, con el texto justificado a ambos lados, como en un procesador de texto.

Las reglas son:

- Cada linea lleva tantas palabras como quepan, con al menos un espacio entre ellas (llenado greedy).
- Los espacios que sobran se reparten lo mas parejo posible entre los huecos. Si no se pueden repartir exacto, los huecos de la izquierda reciben un espacio mas.
- La ultima linea va alineada a la izquierda: un espacio entre palabras y el resto de espacios al final.
- Una linea con una sola palabra tambien va alineada a la izquierda.

## Ejemplos

```
Entrada: words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16
Salida:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
```

```
Entrada: words = ["What","must","be","acknowledgment","shall","be"], maxWidth = 16
Salida:
[
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]
```

La ultima linea queda "shall be" con los espacios al final, y "acknowledgment" va sola en su linea, asi que tambien se alinea a la izquierda.

```
Entrada: words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], maxWidth = 20
Salida:
[
  "Science  is  what we",
  "understand      well",
  "enough to explain to",
  "a  computer.  Art is",
  "everything  else  we",
  "do                  "
]
```

## Restricciones

- `1 <= words.length <= 300`
- `1 <= words[i].length <= 20`
- `words[i]` solo tiene letras del alfabeto ingles y simbolos.
- `1 <= maxWidth <= 100`
- `words[i].length <= maxWidth`

## Solucion

Se recorre la lista armando una linea a la vez. Para decidir cuantas palabras entran se suma el largo de las letras y se cuenta un espacio minimo por cada hueco: la palabra `j` cabe si `letras + len(words[j]) + (palabras ya puestas) <= maxWidth`.

Con las palabras de la linea elegidas hay dos casos. Si es la ultima linea o tiene una sola palabra, se unen con un espacio y se rellena con espacios a la derecha. Si no, los espacios disponibles (`maxWidth - letras`) se dividen entre los huecos: cada hueco recibe la division entera y los primeros `resto` huecos reciben uno extra.

No hay un algoritmo especial que descartar: el reto es cuidar los casos de la ultima linea y de una sola palabra. Cada palabra se procesa una vez.

## Complejidad

- Tiempo: O(n * maxWidth), donde n es el numero de palabras, para armar todas las lineas
- Espacio: O(maxWidth) extra por linea, sin contar la salida
