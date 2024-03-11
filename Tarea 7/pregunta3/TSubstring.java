package pregunta3;

public class TSubstring {

    public static String getTSubstring(String s) {
        int n = s.length();
        int[] sizeOfT = new int[n];
        int len = 0;

        for (int idx = 1; idx < n; idx++) {
            if (s.charAt(idx) == s.charAt(len)) {
                len++;
                sizeOfT[idx] = len;
                continue;
            }

            if (len > 0)
                len = sizeOfT[len - 1];

        }

        return s.substring(0, sizeOfT[n - 1]);
    }

    public static void main(String[] args) {
        String s = "ABRADACADABRA";
        System.out.println(getTSubstring(s));

        s = "AREPERA";
        System.out.println(getTSubstring(s));

        s = "ALGORITMO";
        System.out.println(getTSubstring(s));

        s = "A";
        System.out.println(getTSubstring(s));

    }
}