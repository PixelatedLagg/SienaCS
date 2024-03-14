namespace Siena //45 minutes
{
    public enum Direction
    {
        North,
        South,
        East,
        West
    }

    public class Move
    {
        public Direction Dir;
        public int Spaces;
    }

    public class Program
    {
        static int x = 0, y = 0;
        static char[,] board = new char[18, 38];
        static char currentChar = (char)('a' - 1);
        static bool NewChar()
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
        static bool NewPosition()
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

        static List<Move> moves = [];
        static Direction currentDirection = Direction.East;

        public static void Main()
        {
            for (int i = 0; i < 18; i++)
            {
                for (int j = 0; j < 38; j++)
                {
                    board[i, j] = ' ';
                }
            }
            board[0, 0] = '#';
            Move current = new();
            string input = Console.ReadLine() ?? "";
            while (input != "Q")
            {
                switch (input)
                {
                    case "F":
                        current = new Move
                        {
                            Dir = currentDirection
                        };
                        break;
                    case "B":
                        current = new Move
                        {
                            Dir = currentDirection switch
                            {
                                Direction.North => Direction.South,
                                Direction.South => Direction.North,
                                Direction.East => Direction.West,
                                _ => Direction.East //west
                            }
                        };
                        break;
                    case "L":
                        currentDirection = currentDirection switch
                        {
                            Direction.North => Direction.West,
                            Direction.South => Direction.East,
                            Direction.East => Direction.North,
                            _ => Direction.South //west
                        };
                        break;
                    case "R":
                        currentDirection = currentDirection switch
                        {
                            Direction.North => Direction.East,
                            Direction.South => Direction.West,
                            Direction.East => Direction.South,
                            _ => Direction.North //west
                        };
                        break;
                    default: //int
                        current.Spaces = Convert.ToInt32(input);
                        moves.Add(current);
                        break;
                }
                input = Console.ReadLine() ?? "";
            }
            currentDirection = Direction.East;
            foreach (Move move in moves)
            {
                currentDirection = move.Dir;
                for (int i = 0; i < move.Spaces; i++)
                {
                    if (!NewPosition())
                    {
                        goto end;
                    }
                    else
                    {
                        if (!NewChar())
                        {
                            goto end;
                        }
                        else
                        {
                            board[x, y] = currentChar;
                        }
                    }
                }
            }
            end:
            {
                Console.WriteLine(new string('*', 40));
                for (int i = 0; i < 18; i++)
                {
                    Console.Write('*');
                    for (int j = 0; j < 38; j++)
                    {
                        Console.Write(board[i, j]);
                    }
                    Console.WriteLine('*');
                }
                Console.WriteLine(new string('*', 40));
            }
        }
    }
}