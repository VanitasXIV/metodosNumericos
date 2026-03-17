function df(f: (x: number) => number, x: number, h: number = 1e-7): number {
  return (f(x + h) - f(x - h)) / (2 * h);
}

export function metodoNewton(
  f: (x: number) => number,
  x0: number,
  epsilon: number,
  maxIter: number,
): number {
  let x1 = x0;
  let x2 = x1 - f(x1) / df(f, x1);
  let iter = 0;

  while (Math.abs(x2 - x1) >= epsilon && iter < maxIter) {
    x1 = x2;
    x2 = x1 - f(x1) / df(f, x1);
    iter++;
  }

  return x2;
}
