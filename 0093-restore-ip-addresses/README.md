# 93. Restore IP Addresses

- **Dificultad:** Media
- **Enlace:** https://leetcode.com/problems/restore-ip-addresses/

## Problema

Se recibe una cadena de digitos `s` y hay que encontrar todas las direcciones IP validas que se pueden formar poniendo tres puntos en ella, sin mover ni quitar digitos.

Una IP valida tiene exactamente cuatro numeros separados por puntos. Cada numero va de 0 a 255 y no puede tener ceros a la izquierda: `"0"` sirve, pero `"01"` o `"00"` no. Las direcciones se pueden devolver en cualquier orden.

## Ejemplos

```
Entrada: s = "25525511135"
Salida: ["255.255.11.135","255.255.111.35"]
```

```
Entrada: s = "0000"
Salida: ["0.0.0.0"]
```

```
Entrada: s = "101023"
Salida: ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]
```

## Restricciones

- `1 <= s.length <= 20`
- `s` solo tiene digitos.

## Solucion

Backtracking: se van eligiendo las cuatro partes de izquierda a derecha. En cada paso se prueba tomar 1, 2 o 3 digitos desde la posicion actual, y solo se sigue si ese pedazo es valido (sin cero a la izquierda y como maximo 255). Cuando ya hay cuatro partes, la combinacion sirve solo si se usaron todos los digitos.

Antes de empezar se descartan las cadenas con menos de 4 o mas de 12 digitos, que nunca pueden formar una IP. Como cada parte tiene a lo sumo 3 opciones y son 4 partes, hay como maximo 3^4 = 81 caminos, asi que el trabajo esta acotado.

## Complejidad

- Tiempo: O(1), a lo sumo 81 combinaciones de cadenas de hasta 12 digitos
- Espacio: O(1) sin contar la salida
