import java.security.*;
import java.security.spec.*;
import java.security.interfaces.*;
import java.math.BigInteger;
import javax.crypto.*;
import java.util.Arrays;
import java.nio.file.*;

public class Decrypt {

    public static String readFile(String filename) {
        try {
            return new String(Files.readAllBytes(Paths.get(filename)));
        } catch (Exception e) {
            e.printStackTrace();
        }
        return null;
    }

    public static void main(String[] args) {
        BigInteger _c = new BigInteger(readFile("c.txt"), 10);
        BigInteger _n = new BigInteger(readFile("n.txt"), 10);
        BigInteger _d = new BigInteger(readFile("d.txt"), 16);
        //BigInteger _e = new BigInteger("10001", 16);

        RSAPrivateKeySpec privateKeySpec = new RSAPrivateKeySpec(_n, _d);
        byte[] plaintext = null;
        try {
            KeyFactory keyFactory = KeyFactory.getInstance("RSA");
            RSAPrivateKey privatekey = (RSAPrivateKey) keyFactory.generatePrivate(privateKeySpec);
            Cipher cipher = Cipher.getInstance("RSA/ECB/NoPadding");
            cipher.init(Cipher.DECRYPT_MODE, privatekey);
            plaintext = cipher.doFinal(_c.toByteArray());
        } catch (IllegalBlockSizeException | BadPaddingException | InvalidKeyException | NoSuchPaddingException | NoSuchAlgorithmException | InvalidKeySpecException e) {
            e.printStackTrace();
        }
        System.out.println(Arrays.toString(plaintext));
    }
}