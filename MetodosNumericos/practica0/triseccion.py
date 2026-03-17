from biseccion import sgn
import math

def triseccion(f,a,b, epsilon, verbose=False):
    """
    Halla una raíz de f en [a, b] por trisección.
    En cada paso divide el intervalo en 3 partes iguales
    y elige el subintervalo que contiene la raíz.
    Criterio de parada: b - a < epsilon.

    Parámetros:
        f       : callable — función continua que cambia de signo en [a, b]
        a, b    : float    — extremos del intervalo inicial
        epsilon : float    — error máximo admisible
        verbose : bool     — muestra tabla de pasos (default: False)

    Retorna una aproximación de la raíz con error menor a epsilon.
    """
    
    if verbose:
        print(f"{'Paso':>5} {'a':>12} {'b':>12} {'c1':>12} {'c2':>12}")
        print("-" * 65)
    paso=0
    while b - a >= epsilon:
        c1 = a (b - a) / 3
        c2= a + 2 * (b - a) / 3
        
        if verbose:
            print(f"{paso:>5} {a:>12.6f} {b:>12.6f} {c1:>12.6f} {c2:>12.6f}")
        if f(c1) == 0:
            return c1
        if f(c2) == 0:
            return c2
        elif sgn(f(a)) * sgn(f(c1)) < 0:
            b = c1
        elif sgn(f(c1)) * sgn(f(c2)) < 0:
            a, b = c1, c2
        else:
            a= c2
        paso += 1
    return (a + b) / 2