import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        // put your code here
        Scanner scanner = new Scanner(System.in);
        int nNumbers = Integer.parseInt(scanner.nextLine());
        String numbers = scanner.nextLine();
        String[] strings = numbers.split(" ");
        int sum = 0;
        for (int i = 0; i < nNumbers; i++) {
            sum += Integer.parseInt(strings[i]);
        }
        System.out.println(sum);
    }
}