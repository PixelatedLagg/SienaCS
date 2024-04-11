import java.util.Arrays;
import java.util.Comparator;
import java.util.Scanner;

class Program
{
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);
        int[] speeds = new int[3];
        int[] positions = new int[3];
        speeds[0] = sc.nextInt();
        positions[0] = sc.nextInt();
        speeds[1] = sc.nextInt();
        positions[1] = sc.nextInt();
        speeds[2] = sc.nextInt();
        positions[2] = sc.nextInt();
        sc.close();
        
        Double[] times = new Double[3];
        for (int i = 0; i < 3; i++)
        {
            times[i] = Double.valueOf(100 - positions[i]) / speeds[i];
        }
        
        int[] places = new int[] {0, 0, 0};
        for (int i = 0; i < 3; i++)
        {
            if (max(places) <)
        }
    }
    static int max(int[] array)
    {
        int x = array[0];
        for (int i = 0; i < 3; i++)
        {
            if (array[i] > x)
            {
                x = array[i];
            }
        }
        return x;
    }
}