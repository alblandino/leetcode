# 7. Reverse Integer

- **Dificultad:** Media
- **Enlace:** https://leetcode.com/problems/reverse-integer/

## Problema

Se recibe un entero `x` de 32 bits con signo y hay que devolverlo con sus digitos invertidos, conservando el signo. Los ceros que queden al inicio desaparecen (120 pasa a ser 21).

Si el numero invertido se sale del rango de 32 bits con signo, `[-2^31, 2^31 - 1]`, se devuelve 0. Hay que suponer que el entorno no permite guardar enteros de 64 bits, asi que no vale calcular el resultado completo y revisarlo al final.

## Ejemplos

```
Entrada: x = 123
Salida: 321
```

```
Entrada: x = -123
Salida: -321
```

```
Entrada: x = 120
Salida: 21
```

## Restricciones

- `-2^31 <= x <= 2^31 - 1`

## Solucion

Se trabaja con el valor absoluto y se guarda el signo aparte. Se sacan los digitos de derecha a izquierda con `% 10` y `// 10`, y se van agregando al resultado con `result * 10 + digit`.

Para respetar la regla de 32 bits, antes de agregar cada digito se comprueba que `result * 10 + digit` no pase de `2^31 - 1`. Despejando, se sale del rango cuando `result > (INT_MAX - digit) // 10`, y en ese caso se devuelve 0 sin llegar a calcular el valor grande. Para los negativos alcanza con el mismo limite: el unico caso que lo usaria es una magnitud invertida igual a `2^31`, y para eso la entrada tendria que ser -8463847412, que no es un `x` valido.

Convertir a texto e invertir la cadena tambien funciona, pero no muestra el manejo del desbordamiento que es lo que busca el ejercicio.

## Complejidad

- Tiempo: O(log |x|), uno por digito
- Espacio: O(1)
