# Ejercicio Final!
Final-Método de Newton Raphson

Modifica el programa que se encuentra en la carpeta `src` que se llama `exercise.py` y que contiene el siguiente código:

```python
def main():
  #escribe tu código abajo de esta línea
  pass

if __name__ == '__main__':
    main()
```

La línea `#escribe tu código abajo de esta línea` es un comentario, el programa la va a ignorar al ejecutarse.

Programa el método de Newton Raphson para encontrar la raíz de la función `f(x)=exp(-x) - x`. 

Analiza cuidadosamente el código inicial que se te proporciona y agrega el código que implemente el método.

Los valores de entrada (**inicial** y **error**) al método deberán ser `flotantes`.

La salida del programa debe de ser exactamente de la siguiente forma:

```
Método de Newton Raphson
------------------------
Dame el valor inicial:0
Dame el error:0.05
La raíz de la función y=f(x) es 0.5671 calculada en 3 iteraciones con Newton-Raphson
Las aproximaciones fueron: [0.0, 0.5, 0.5663110031972182, 0.5671431650348622]
```

**Nota:** No te preocupes por esta parte del código `if __name__ == '__main__':` por el momento. No la vamos a necesitar para este programa, pero es una buena práctica incluirla y quedará más claro para que sirve en los siguientes ejercicios.

Una vez que termines tu actividad y la hayas probado con `pytest`, subela a tu repositorio en GitHub, con el proceso de commit + push.
