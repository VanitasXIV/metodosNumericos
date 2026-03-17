import math

def iterar(f, x, n):
    """
    Aplica f composicionalmente n veces sobre x.
    
    Parámetros:
        f: callable - la funcion a iterar
        x: float - valor inicial
        n: int - numero de iteraciones
        
    Retorna el resultado de f(f(f(... f(x)...))) (n veces).
    """
    resultado = x
    for i in range(n):
        resultado = f(resultado)
    return resultado

print(iterar(math.cos, 1.0, 100)) # -> aprox 0.7390851332 número de Dottie, único punto fijo del coseno en radianes donde cos(x) = x
print(iterar(lambda x: x**2 - 1, 0, 6)) # ciclo: 0 o -1
print(iterar(lambda x: math.sqrt(abs(x)), 256, 20)) # -> 1.0
