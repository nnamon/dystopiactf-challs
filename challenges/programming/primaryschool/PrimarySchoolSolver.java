import java.io.ByteArrayOutputStream;
import java.math.BigInteger;
import java.util.*;
import javax.crypto.Cipher;
import javax.crypto.spec.*;

public class PrimarySchoolSolver {
    private static byte[] flagBytes = new BigInteger("3a8efadcc8531f6ee3e5eaeed174d34d", 16).toByteArray();

    public static void main(String[] args) throws Exception {
        int N = 1000000000;
        long total = 0;
        List<Integer> primeNumbers = new ArrayList<>();

        boolean[] isPrime = new boolean[N + 1];
        for (int i = 2; i <= N; i++)
            isPrime[i] = true;

        for (int i = 2; i * i <= N; i++)
            if (isPrime[i])
                for (int j = i; i * j <= N; j++)
                    isPrime[i * j] = false;

        for (int i = 2; i <= N; i++) {
            if (isPrime[i]) {
                primeNumbers.add(i);
                total += i;
            }
        }

        byte[] keyBytes;
        byte[] nullBytes = new byte[16];
        Arrays.fill(nullBytes, (byte) 0);

        ByteArrayOutputStream baos = new ByteArrayOutputStream(16);

        for (int a = 0; a < (primeNumbers.size() % 4) - 1; a++)
            total -= primeNumbers.get(primeNumbers.size() - 1 - a);

        for (int i = primeNumbers.size() - (primeNumbers.size() % 4); i >= 0; i--) {
            if ((i + 1) % 4 == 0) {
                baos.reset();
                byte[] sumBytes = BigInteger.valueOf(total).toByteArray();

                baos.write(nullBytes, 0, 16 - sumBytes.length);
                baos.write(sumBytes, 0, sumBytes.length);
                keyBytes = baos.toByteArray();
                flagBytes = decrypt(keyBytes, flagBytes);
            }
            total -= primeNumbers.get(i);
        }
        System.out.println("Flag: " + new String(flagBytes));
    }

    public static byte[] decrypt(byte[] keyBytes, byte[] flagBytes) throws Exception {
        Cipher cipher = Cipher.getInstance("AES/ECB/NoPadding");
        cipher.init(Cipher.DECRYPT_MODE, new SecretKeySpec(keyBytes, "AES"));
        return cipher.doFinal(flagBytes);
    }

    public static String bytesToHex(byte[] bytes) {
        StringBuilder builder = new StringBuilder();
        for(byte b : bytes)
            builder.append(String.format("%02x", b));
        return builder.toString();
    }
}