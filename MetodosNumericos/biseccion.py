import math

def sgn(z):
    if z == 0:   return 0
    elif z > 0:  return 1
    else:        return -1

def biseccion(f, a, b, epsilon, verbose=False):
    """
    Halla una raíz de f en [a, b] por bisección.
    Criterio de parada: b - a < epsilon.

    Parámetros:
        f       : callable — función continua que cambia de signo en [a, b]
        a, b    : float    — extremos del intervalo inicial
        epsilon : float    — error máximo admisible
        verbose : bool     — muestra tabla de pasos (default: False)

    Retorna una aproximación de la raíz con error menor a epsilon.
    """
    if verbose:
        print(f"{'Paso':>5} {'a':>12} {'b':>12} {'c':>12} {'f(c)':>12}")
        print("-" * 55)
    paso = 0
    while b - a >= epsilon:
        c = (a + b) / 2
        if verbose:
            print(f"{paso:>5} {a:>12.6f} {b:>12.6f} {c:>12.6f} {f(c):>12.6f}")
        if f(c) == 0:
            return c
        elif sgn(f(c)) * sgn(f(a)) < 0:
            b = c
        else:
            a = c
        paso += 1
    return c

# === 4. x³ + x - 5 = 0, [1,2], ε = 0.5 ===
f4 = lambda x: x**3 + x - 5
print(biseccion(f4, 1, 2, epsilon=0.5, verbose=True))

# === 5. x³ + x - 10 = 0, 4 pasos → intervalo [1,2] longitud 1, epsilon = 1/2^4 = 0.0625 ===
f5 = lambda x: x**3 + x - 10
print(biseccion(f5, 1, 2, epsilon=0.0625, verbose=True))

# === 6. x² + x - 12 = 0, raíz exacta = 3 ===
f6 = lambda x: x**2 + x - 12
aprox = biseccion(f6, 1, 4, epsilon=0.01, verbose=True)
exacto = (-1 + math.sqrt(1 + 48)) / 2  # = 3.0
print(f"Aproximado: {aprox}  Exacto: {exacto}  Error: {abs(aprox - exacto):.6f}")

# === 7. cos(x) = -1 → cos(x) cruza cero en π, usar [1,4], ε = 0.1 ===
f7 = lambda x: math.cos(x)
aprox_pi = biseccion(f7, 1, 4, epsilon=0.1, verbose=True)
print(f"Aproximación de π: {aprox_pi}  Error: {abs(aprox_pi - math.pi):.6f}")