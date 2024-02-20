import * as rl from "readline-sync";

interface VirtualArray {
  t?: Array<number>;
  ctr: number;
  a?: Array<number>;
  b?: Array<number>;
}


// Creamos una estructura vacia para el virtual array de largo n
function createVirtualArray(n: number) {
  let virtualArray: VirtualArray = { ctr: 0 };

  if (n <= 0) return virtualArray;

  virtualArray = {
    ...virtualArray,
    t: new Array(n),
    a: new Array(n),
    b: new Array(n),
  };

  return virtualArray;
}

// Chequeamos si una posicion es valida en un array
function validPosition(n: number, idx: number) {
  return idx >= 0 && idx < n;
}

// Inicializamos t
function initialize(virtualArray: VirtualArray, idx: number, val: number) {
  if (!validPosition(Number(virtualArray.t?.length), idx)) {
    console.error("Posicion no valida");
    return virtualArray;
  }

  const ctr = virtualArray.ctr + 1;
  const t = [...(virtualArray.t ?? [])];
  const a = [...(virtualArray.a ?? [])];
  const b = [...(virtualArray.b ?? [])];

  t[idx] = val;
  a[ctr] = idx;
  b[idx] = ctr;

  return { ctr: ctr, t: t, a: a, b: b };
}

function clean(virtualArray: VirtualArray) {
  return createVirtualArray(virtualArray.t?.length ?? 0);
}

function isInitialized(virtualArray: VirtualArray, idx: number) {
  if (!validPosition(Number(virtualArray.t?.length), idx)) {
    console.error("Posicion no valida");
    return;
  }

  if (
    !virtualArray.b ||
    virtualArray.b[idx] < 1 ||
    virtualArray.b[idx] > virtualArray.ctr
  )
    return false;

  if (!virtualArray.a || virtualArray.a[virtualArray.b[idx]] != idx)
    return false;

  return true;
}

function main() {
  const args = process.argv.slice(2);
  const sizeArg = args.find((arg) => arg.startsWith("--n="));
  const size = sizeArg ? Number(sizeArg.split("=")[1]) : undefined;

  if (!size || size < 0) {
    console.error(
      "El programa debe ser inicializado como 'npm run start -- --n=<number>' con un n entero mayor o igual a 0"
    );
    return;
  }

  let more = 1;
  let vA = createVirtualArray(size);
  let splittedAnswer: Array<string>;
  let pos: number;
  let val: number;

  while (more) {
    let answer: string = rl.question("Inserte un comando: ").toLowerCase();
    if (answer == "salir") {
      more = 0;
      console.log("Hasta luego");
    } else if (answer == "limpiar") {
      more++;
      vA = clean(vA);
      console.log(vA);
    } else if (answer.startsWith("consultar")) {
      more++;
      splittedAnswer = answer.split(" ");
      if (splittedAnswer.length < 2) {
        console.error("El formato correcto es CONSULTAR POS");
      } else {
        pos = Number(splittedAnswer[1]) - 1;
        if (!!vA.t && isInitialized(vA, pos)) {
          console.log(vA.t[pos]);
        } else {
          console.log("No esta inicializado");
        }
      }
    } else if (answer.startsWith("asignar")) {
      more++;
      splittedAnswer = answer.split(" ");

      if (splittedAnswer.length < 3) {
        console.error("El formato correcto es CONSULTAR POS VAL");
      } else {
        pos = Number(splittedAnswer[1]) - 1;
        val = Number(splittedAnswer[2]);
        vA = initialize(vA, pos, val);
      }
    } else {
      console.error("No es un comando valido");
    }
  }
}

main();
