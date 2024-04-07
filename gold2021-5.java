import java.util.ArrayList;
import java.util.Scanner;

class point
{
    public point(int i, int j)
    {
        x = i;
        y = j;
    }
    public void Print()
    {
        System.out.println("(" + x + ", " + y + ")");
    }

    public int x;
    public int y;
}

class Program
{
    static int currentX;
    static int currentY;
    static String top;
    static String bottom;
    static String[] sides = new String[5];

    public static void main(String[] args)
    {
        Character[][] board = new Character[5][5];

        Scanner sc = new Scanner(System.in);
        top = sc.nextLine();
        for (int i = 0; i < 5; i++)
        {
            sides[i] = sc.nextLine();
        }
        bottom = sc.nextLine();
        currentX = sc.nextInt();
        currentY = sc.nextInt();
        sc.close();

        Boolean[][] taken = fullFalse();
        taken[currentX][currentY] = true;
        board[currentX][currentY] = 'A';
    
        System.out.println(recursiveCheck('B', 1, 2, deepClone(taken)));
        /*for (int letter = 'B'; letter < 'B' + 23; letter++)
        {
            ArrayList<point> points = surrounding(currentX, currentY, taken);
            for (point p : points)
            {
                if (recursiveCheck((char)letter, p.x, p.y, taken.clone()))
                {
                    board[p.x][p.y] = (char)letter;
                    taken[p.x][p.y] = true;
                    currentX = p.x;
                    currentY = p.y;
                    break;
                }
            }
            System.out.println((char)letter);
        }

        for (int x = 0; x < 5; x++)
        {
            for (int y = 0; y < 5; y++)
            {
                System.out.print(board[x][y]);
            }
            System.out.println();
        }*/
    }

    static Boolean recursiveCheck(Character letter, int x, int y, Boolean[][] taken)
    {
        if (letter == 'Z')
        {
            return true;
        }
        ArrayList<point> points = surrounding(x, y, taken);
        taken[x][y] = true;
        int clueX = getClueX(letter);
        int clueY = getClueY(letter);
        for (point p : points)
        {
            if (clueTest(p, clueX, clueY) && recursiveCheck((char)(letter + 1), p.x, p.y, deepClone(taken)))
            {
                return true;
            }
        }
        return false;
    }

    static Boolean clueTest(point p, int clueX, int clueY)
    {
        if (clueY == -1) //x clue
        {
            if (clueX == 0) //tl diagonal
            {
                return p.x == p.y;
            }
            if (clueX == 5) //tr diagonal
            {
                return p.x + p.y == 4;
            }
            return p.x == clueX;
        }
        else //y clue
        {
            return p.y == clueY - 1;
        }
    }

    public static ArrayList<point> surrounding(int x, int y, Boolean[][] taken)
    {
        ArrayList<point> points = new ArrayList<point>();
        for (int i = currentX - 1; i < currentX + 2; i++)
        {
            if (i == -1 || i == 5)
            {
                continue;
            }
            for (int j = currentY - 1; j < currentY + 2; j++)
            {
                if (j == -1 || j == 5 || taken[i][j] || (i == x && j == y))
                {
                    continue;
                }
                points.add(new point(i, j));
            }
        }
        return points;
    }

    static int getClueX(Character letter)
    {
        for (int i = 0; i < 5; i++)
        {
            if (sides[i].indexOf(letter) != -1)
            {
                return i;
            }
        }
        return -1;
    }

    static int getClueY(Character letter)
    {
        if (bottom.indexOf(letter) == -1)
        {
            return top.indexOf(letter);
        }
        else
        {
            return bottom.indexOf(letter);
        }
    }

    static Boolean[][] fullFalse()
    {
        Boolean[][] result = new Boolean[5][5];
        for (int i = 0; i < 5; i++)
        {
            for (int j = 0; j < 5; j++)
            {
                result[i][j] = false;
            }
        }
        return result;
    }

    static Boolean[][] deepClone(Boolean[][] original)
    {
        Boolean[][] clone = new Boolean[original.length][original[0].length];
        for (int i = 0; i < original.length; i++) 
        {
            for (int j = 0; j < original[0].length; j++)
            {
                clone[i][j] = original[i][j];
            }
        }
        return clone;
    }
}