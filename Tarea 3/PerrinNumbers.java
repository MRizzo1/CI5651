/**
 * Programa para obtener los numeros de Perrin aprovechando la version mejorada
 * de exponenciar una matrix.
 * 
 * @author Mariangela Rizzo
 */
public class PerrinNumbers {

    /**
     * Obtiene los numeros de Perrin usando exponenciacion de matrices
     * 
     * @param n El Perrin(n) que se quiere obtener
     * @return El numero de Perrin para n.
     */
    static int fastPerrin(int n) {
        // Matrices para obtener el numero de Perrin
        int P[][] = new int[][] { { 0, 1, 0 }, { 0, 0, 1 }, { 1, 1, 0 } };
        int BASE[][] = new int[][] { { 3 }, { 0 }, { 2 } };

        // Manejamos los casos base aparte
        if (n >= 0 && n < 3)
            return BASE[n][0];

        // Exponenciamos la matriz acorde a la formula
        fastExponentiation(P, n - 2);

        // Multiplicamos el resultado por la base y P(n) siemore va a ser el ultimo argumento de la matriz resultante
        // Es decir, (P(n + 2))
        int result[][] = multiplyBASE(P, BASE);

        return result[2][0];
    }

    /**
     * Version rapida de la exponenciacion de matrices
     * 
     * @param P Matriz a exponenciar, regresa exponenciada en si misma
     * @param n El numero al que queremos exponenciar la matriz
     * @return No retorna nada
     */
    static void fastExponentiation(int P[][], int n) {

        int BasePCopy[][] = { { 0, 1, 0 }, { 0, 0, 1 }, { 1, 1, 0 } };
        if (n != 1) {
            fastExponentiation(P, n / 2);
            multiply3x3(P, P);

            if (n % 2 != 0)
                multiply3x3(P, BasePCopy);
        }

        return;

    }

    /**
     * Multiplicamos matrices de la forma 3x3 y 3x1
     * 
     * @param M1 Primera matriz a multiplicar de la forma 3x3
     * @param M2 Segunda matriz a multiplicar de la forma 3x1
     * @return Resultado de la multiplicacion
     */
    static int[][] multiplyBASE(int M1[][], int M2[][]) {

        int result[][] = new int[3][1];

        for (int i = 0; i < 3; i++) {
            result[i][0] = 0;
            for (int j = 0; j < 3; j++) {
                result[i][0] += M1[i][j] * M2[j][0];
            }
        }

        return result;

    }

    /**
     * Multiplicamos matrices de la forma 3x3 y 3x3
     * 
     * @param M1 Primera matriz a multiplicar de la forma 3x3, se retorna el resultado de la multiplicacion sustituyendo esta matriz
     * @param M2 Segunda matriz a multiplicar de la forma 3x3
     * @return Nada
     */
    static void multiply3x3(int M1[][], int M2[][]) {

        int result[][] = new int[3][3];
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                result[i][j] = 0;
                for (int k = 0; k < 3; k++) {
                    result[i][j] += M1[i][k] * M2[k][j];
                }
            }
        }

        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                M1[i][j] = result[i][j];
            }
        }

    }

    /* Driver program to test above function */
    public static void main(String args[]) {
        System.out.println(fastPerrin(2));
        System.out.println(fastPerrin(3));
        System.out.println(fastPerrin(10));
        System.out.println(fastPerrin(17));
        System.out.println(fastPerrin(75));

    }
};
