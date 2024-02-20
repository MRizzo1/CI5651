interface VirtualA {
  T: Array<number>;
}

// Obtener todos los divisores de un numero hasta cierto limite
function getDivisorsUntilLimit(n: number, limit: number) {
  const divisors: Array<number> = new Array();
  while (limit >= 1) {
    if (n % limit == 0) {
      divisors.push(limit);
    }
    --limit;
  }

  return divisors;
}

// Contar las subsecuencias de un array que cumplan con lo establecido en el problema
function countSubsequence(A: Array<number>) {
  const n: number = A.length;

  // Considerando el vacio sin agregarlo al resultado
  const Bsum: Array<number> = [1, ...new Array(n).fill(0)];

  let result: number = 0;
  let divisors: Array<number>;
  let divisor: number;

  for (let i: number = 0; i < n; i++) {
    divisors = getDivisorsUntilLimit(A[i], i + 1);
    // Para cada divisor (digamos numero `div`) del elemento A[i] en el rango [1, i + 1] 
    // A[i] puede ser el numero en la posicion numero `div` en la subsecuencia B de largo i + 1 considerada
    for (let j: number = 0; j < divisors.length; j++) {
      divisor = divisors[j];
      result += Bsum[divisor - 1];
      Bsum[divisor] += Bsum[divisor - 1];
    }

  }

  return result;
}

const A: Array<number> = [2, 2, 1, 22, 15];
console.log(countSubsequence(A));
