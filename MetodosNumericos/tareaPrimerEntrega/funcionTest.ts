import { metodoNewton } from "./metodoNewton";
import { triseccion } from "./triseccionTS";


const f = (x: number) : number =>
    x**6 - 7*x**4 + 14*x**2 -8;

const epsilon = 1e-8;

const raizNewton = metodoNewton(f, 1.5, epsilon, 100);
const raizTriseccion = triseccion(f, 1, 2, epsilon);

console.log(`Raiz aproximada por Newton: ${raizNewton}`);
console.log(`Raiz aproximada por triseccion: ${raizTriseccion}`)