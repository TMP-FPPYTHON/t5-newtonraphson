import math

def newton_raphson(f, fp, x, error):
    # Parametros de entrada:
    # f -> Funcion a encontrar la raíz
    # fp-> Primera derivada de la función a encontra la raíz
    # x-> Aproximaciones a la raíz
    # error-> Criterio de parada: cuando el valor absoluto de dos aproximaciones consecutivas sea menor que este valor el algoritmo para

    # Valores de salida:
    # raiz (r), aproximaciones (lista de aproximaciones), número de iteraciones (i)

    erroractual = math.inf
    i = 0
    while erroractual > error:
        x = x + [x[i]-f(x[i])/fp(x[i])]
        erroractual = math.fabs(x[i+1]-x[i])
        i=i+1
    return x[i], x, i

def main():
    #escribe tu código abajo de esta línea

    # Funcion Lambda y=f(x) a aplicar el metodo
    f = lambda x : math.exp(-x) - x

    # Funcion Lambda y'=f'(x) a utilizar en el metodo
    fp = lambda x : -math.exp(-x) - 1

    # Encabezado del método
    print("Método de Newton Raphson")
    print("------------------------")

    # Aproximacion inicial
    x=[0]
    x[0] = float(input("Dame el valor inicial:"))
    error = float(input("Dame el error:"))

    raiz,x,iteraciones = newton_raphson(f, fp, x, error)

    print(f"La raíz de la función y=f(x) es {raiz:6.4f} calculada en {iteraciones} iteraciones con Newton-Raphson")
    print(f"Las aproximaciones fueron: {x}")

if __name__=='__main__':
    main()
