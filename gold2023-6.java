import java.util.ArrayList;
import java.util.Scanner;

class Move
{
    public Direction Dir;
    public int Spaces;
}

enum Direction
{
    North,
    South,
    East,
    West
}

class Program
{
    static int x = 0, y = 0;
    static char[][] board = new char[18][38];
    static char currentChar = (char)('a' - 1);

    static Boolean NewChar()
    {
        switch (currentChar)
        {
            case 'z':
                currentChar = 'A';
                return true;
            case 'Z':
                return false;
            default:
                currentChar++;
                return true;
        }
    }
    static Boolean NewPosition()
    {
        switch (currentDirection)
        {
            case Direction.East: //east
                if (y == 37)
                {
                    return false;
                }
                y++;
                break;
            case Direction.North: //north
                if (x == 0)
                {
                    return false;
                }
                x--;
                break;
            case Direction.West: //west
                if (y == 0)
                {
                    return false;
                }
                y--;
                break;
            case Direction.South: //south
                if (x == 17)
                {
                    return false;
                }
                x++;
                break;
        }
        return true;
    }

    static ArrayList<Move> moves = new ArrayList<Move>();
    static Direction currentDirection = Direction.East;

    public static void main(String[] args)
    {
        for (int i = 0; i < 18; i++)
        {
            for (int j = 0; j < 38; j++)
            {
                board[i][j] = ' ';
            }
        }
        board[0][0] = '#';
        Move current = new Move();
        Scanner sc = new Scanner(System.in);
        String input = sc.nextLine();
        while (input != "Q")
        {
            switch (input)
            {
                case "F":
                    current = new Move();
                    current.Dir = currentDirection;
                    break;
                case "B":
                    current = new Move();
                    switch (currentDirection)
                    {
                        case Direction.North:
                            current.Dir = Direction.South;
                            break;
                        case Direction.South:
                            current.Dir = Direction.North;
                            break;
                        case Direction.East:
                            current.Dir = Direction.West;
                            break;
                        case Direction.West:
                            current.Dir = Direction.East;
                            break;
                    }
                    break;
                case "L":
                    switch (currentDirection)
                    {
                        case Direction.North:
                            currentDirection = Direction.West;
                            break;
                        case Direction.South:
                            currentDirection = Direction.East;
                            break;
                        case Direction.East:
                            currentDirection = Direction.North;
                            break;
                        case Direction.West:
                            currentDirection = Direction.South;
                            break;
                    }
                    break;
                case "R":
                    switch (currentDirection)
                    {
                        case Direction.North:
                            currentDirection = Direction.East;
                            break;
                        case Direction.South:
                            currentDirection = Direction.West;
                            break;
                        case Direction.East:
                            currentDirection = Direction.South;
                            break;
                        case Direction.West:
                            currentDirection = Direction.North;
                            break;
                    }
                    break;
                default: //int
                    if (input == "Q")
                    {
                        break;
                    }
                    current.Spaces = Integer.parseInt(input);
                    moves.add(current);
                    break;
            }
            input = sc.nextLine();
        }
        sc.close();
        currentDirection = Direction.East;
        for (Move move : moves)
        {
            currentDirection = move.Dir;
            for (int i = 0; i < move.Spaces; i++)
            {
                if (!NewPosition())
                {
                    System.out.println("*".repeat(40));
                    for (int x = 0; x < 18; x++)
                    {
                        System.out.println('*');
                        for (int j = 0; j < 38; j++)
                        {
                            System.out.println(board[x][j]);
                        }
                        System.out.println('*');
                    }
                    System.out.println("*".repeat(40));
                }
                else
                {
                    if (!NewChar())
                    {
                        System.out.println("*".repeat(40));
                        for (int x = 0; x < 18; x++)
                        {
                            System.out.println('*');
                            for (int j = 0; j < 38; j++)
                            {
                                System.out.println(board[x][j]);
                            }
                            System.out.println('*');
                        }
                        System.out.println("*".repeat(40));
                    }
                    else
                    {
                        board[x][y] = currentChar;
                    }
                }
            }
        }
        System.out.println("*".repeat(40));
        for (int i = 0; i < 18; i++)
        {
            System.out.println('*');
            for (int j = 0; j < 38; j++)
            {
                System.out.println(board[i][j]);
            }
            System.out.println('*');
        }
        System.out.println("*".repeat(40));
    }
}