import math

def newton_raphson(f, fp, x, error):
    # Parametros de entrada:
    # f -> Funcion a encontrar la raíz
    # fp-> Primera derivada de la función a encontra la raíz
    # x-> Aproximaciones a la raíz
    # error-> Criterio de parada: cuando el valor absoluto de dos aproximaciones consecutivas sea menor que este valor el algoritmo para

    # Valores de salida:
    # raiz (r), aproximaciones (lista de aproximaciones), número de iteraciones (i)

    
    return raiz, x, i

def main():
    #escribe tu código abajo

    # Funcion Lambda y=f(x) a aplicar el metodo
    # f = ...

    # Funcion Lambda y'=f'(x) a utilizar en el metodo
    # fp = ...

    # Encabezado del método
    print("Método de Newton Raphson")
    print("------------------------")

    # Solicito datos de entrada (aproximacion inicial y error)
    # ...
    
    # Aplico el metodo de Newton Raphson para encontrar la raiz
    raiz,x,iteraciones = newton_raphson(f, fp, x, error)

    # Muestro resultados
    # ...

if __name__=='__main__':
    main()
