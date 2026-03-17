import math

def iterar_alternando (f,g,x,n):
    """
    Aplica alternadamente f y g sobre x, n veces en total.
    La secuencia es: f, g, f, g, ... (empieza siempre con f).

    Parámetros:
        f, g : callable — funciones a alternar
        x    : float    — valor inicial
        n    : int      — número total de aplicaciones

    Retorna el resultado tras n aplicaciones.
    """
    funciones = [f, g]
    for i in range(n):
        x= funciones[i%2](x)
    return x

#Ejemplos

print(iterar_alternando(math.cos, math.sin, 1.0, 100))
print(iterar_alternando(lambda x: x**2 -1, lambda x: x + 0.5, 0, 10))