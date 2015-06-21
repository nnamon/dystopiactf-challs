import java.io.ByteArrayOutputStream;
import java.math.BigInteger;
import java.util.*;
import javax.crypto.Cipher;
import javax.crypto.spec.*;

public class PrimarySchoolChallenge {
    private static byte[] flagBytes = "Pr1m4r1lY_a_n00B".getBytes();

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

        for (int i = 2; i <= N; i++)
            if (isPrime[i])
                primeNumbers.add(i);

        byte[] keyBytes;
        byte[] nullBytes = new byte[16];
        Arrays.fill(nullBytes, (byte) 0);

        ByteArrayOutputStream baos = new ByteArrayOutputStream(16);

        for (int i = 0; i < primeNumbers.size(); i++) {
            total += primeNumbers.get(i);

            if ((i+1) % 4 == 0) {
                baos.reset();
                byte[] sumBytes = BigInteger.valueOf(total).toByteArray();

                baos.write(nullBytes, 0, 16 - sumBytes.length);
                baos.write(sumBytes, 0, sumBytes.length);
                keyBytes = baos.toByteArray();
                flagBytes = encrypt(keyBytes, flagBytes);
            }
        }
        System.out.println("Encrypted flag: " + bytesToHex(flagBytes));
    }

    public static byte[] encrypt(byte[] keyBytes, byte[] flagBytes) throws Exception {
        Cipher cipher = Cipher.getInstance("AES/ECB/NoPadding");
        cipher.init(Cipher.ENCRYPT_MODE, new SecretKeySpec(keyBytes, "AES"));
        return cipher.doFinal(flagBytes);
    }

    public static String bytesToHex(byte[] bytes) {
        StringBuilder builder = new StringBuilder();
        for(byte b : bytes)
            builder.append(String.format("%02x", b));
        return builder.toString();
    }
}