import java.util.Scanner;

class Program
{
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);
        int w = sc.nextInt();
        int l = sc.nextInt();
        int h = sc.nextInt();
        System.out.println(2 * (w * l + h * l + h * w));
    }
}