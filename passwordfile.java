import java.io.FileWriter;
import java.io.FileReader;
import java.io.BufferedReader;
import java.io.IOException;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.util.ArrayList;
import java.util.List;
import java.util.Random;

public class PasswordHashingExample {

    public static void main(String[] args) {
        try {
            List<String> passwords = generatePasswords(10);

            writePasswordsToFile("passwords.txt", passwords);

            List<String> hashedPasswords = readPasswordsAndHash("passwords.txt");

            writePasswordsToFile("hashed_passwords.txt", hashedPasswords);

            String salt = generateSalt();
            writeSaltToFile("salt.txt", salt);

            String readSalt = readSaltFromFile("salt.txt");

            List<String> hashedPasswordsWithSalt = readPasswordsAndHashWithSalt("passwords.txt", readSalt);

            writePasswordsToFile("hashed_passwords_with_salt.txt", hashedPasswordsWithSalt);

        } catch (IOException e) {
            e.printStackTrace();
        } catch (NoSuchAlgorithmException e) {
            e.printStackTrace();
        }
    }

    public static List<String> generatePasswords(int count) {
        List<String> passwords = new ArrayList<>();
        Random random = new Random();
        for (int i = 0; i < count; i++) {
            String password = "";
            for (int j = 0; j < 8; j++) {
                char randomChar = (char) (random.nextInt(94) + 33);
                password += randomChar;
            }
            passwords.add(password);
        }
        return passwords;
    }

    public static void writePasswordsToFile(String filename, List<String> passwords) throws IOException {
        FileWriter writer = new FileWriter(filename);
        for (String password : passwords) {
            writer.write(password + "\n");
        }
        writer.close();
    }

    public static List<String> readPasswordsAndHash(String filename) throws IOException, NoSuchAlgorithmException {
        List<String> hashedPasswords = new ArrayList<>();
        BufferedReader reader = new BufferedReader(new FileReader(filename));
        String password;
        while ((password = reader.readLine()) != null) {
            String hashedPassword = hashPassword(password);
            hashedPasswords.add(hashedPassword);
        }
        reader.close();
        return hashedPasswords;
    }

    public static String hashPassword(String password) throws NoSuchAlgorithmException {
        MessageDigest md = MessageDigest.getInstance("SHA-256");
        byte[] hashedBytes = md.digest(password.getBytes());
        StringBuilder sb = new StringBuilder();
        for (byte b : hashedBytes) {
            sb.append(Integer.toString((b & 0xff) + 0x100, 16).substring(1));
        }
        return sb.toString();
    }

    public static void writeSaltToFile(String filename, String salt) throws IOException {
        FileWriter writer = new FileWriter(filename);
        writer.write(salt);
        writer.close();
    }

    public static String readSaltFromFile(String filename) throws IOException {
        BufferedReader reader = new BufferedReader(new FileReader(filename));
        String salt = reader.readLine();
        reader.close();
        return salt;
    }
}
