import java.util.ArrayList;
import java.util.Scanner;

class Program
{
    static ArrayList<Integer> candidatesX = new ArrayList<Integer>();
    static ArrayList<Integer> candidatesY = new ArrayList<Integer>();
    static int currentX;
    static int currentY;
    public static void main(String[] args)
    {
        Character[][] board = new Character[5][5];
        Boolean[][] taken = new Boolean[5][5];
        for (int i = 0; i < 5; i++)
        {
            for (int j = 0; j < 5; j++)
            {
                taken[i][j] = false;
            }
        }

        Scanner sc = new Scanner(System.in);
        String top = sc.nextLine();
        String[] sides = new String[5];
        for (int i = 0; i < 5; i++)
        {
            sides[i] = sc.nextLine();
        }
        String bottom = sc.nextLine();
        currentX = sc.nextInt();
        currentY = sc.nextInt();
        sc.close();
    
        for (int letter = 'b'; letter < 'b' + 24; letter++)
        {
            getCandidates();
        }
    }
    public static void getCandidates()
    {
        for (int i = currentX - 1; i < currentX + 2; i++)
        {
            if (i == -1 || i == 6)
            {
                continue;
            }
            for (int j = currentY - 1; j < currentY + 2; j++)
            {
                if (j == -1 || j == 6)
                {
                    continue;
                }
                candidatesX.add(i);
                candidatesY.add(j);
            }
        }
    }
}