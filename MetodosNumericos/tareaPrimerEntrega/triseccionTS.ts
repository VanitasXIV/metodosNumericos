function sgn(x: number): number {
  return x > 0 ? 1 : x < 0 ? -1 : 0;
}

export function triseccion(
  f: (x: number) => number,
  a: number,
  b: number,
  epsilon: number,
): number {
  if (sgn(f(a)) * sgn(f(b)) >= 0) {
    throw new Error("No se cumple la condición de Bolzano: f(a) y f(b) deben tener signos opuestos");
  }

  while (b - a >= epsilon) {
    const c1 = a + (b - a) / 3;
    const c2 = a + (2 * (b - a)) / 3;

    if (f(c1) === 0) return c1;
    if (f(c2) === 0) return c2;
    else if (sgn(f(a)) * sgn(f(c1)) < 0) {
      b = c1;
    } else if (sgn(f(c1)) * sgn(f(c2)) < 0) {
      a = c1;
      b = c2;
    } else {
      a = c2;
    }
  }

  return (a + b) / 2;
}