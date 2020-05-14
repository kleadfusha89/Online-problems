using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace _2d_array
{
    class Program
    {
       /*public int HourglassSum(int[,] arr)
        {
            int rows = arr.GetLength(0);
            int columns = arr.GetLength(1);
            int maxSum = -63;
            int currentSum = -63;

            for (int rw = 0; rw < rows - 2; rw++)
            {
                for (int cl = 0; cl < columns - 2; cl++)
                {
                    currentSum = arr[rw, cl] + arr[rw, cl + 1]
                    + arr[rw, cl + 2] + arr[rw + 1, cl + 1]
                    + arr[rw + 2, cl] + arr[rw + 2, cl + 1]
                    + arr[rw + 2, cl + 2];

                    if (currentSum > maxSum)
                        maxSum = currentSum;

                }
            }

            return maxSum;

        }*/



        static void Main(string[] args)
        {
            int[,] arr = new int[6,4];

            int rows = arr.GetLength(0);
            int columns = arr.GetLength(1);

            Random rnd = new Random();

            for(int i = 0; i < rows;i++)
            {
                for(int j = 0; j < columns; j++)
                {
                    arr[i,j] = rnd.Next(-9, 9);

                }
            }



            for (int m = 0; m < rows; m++)
            {
                for (int n = 0; n < columns; n++)
                {
                   
                    Console.Write(arr[m, n] + "   ");

                    

                }
                Console.WriteLine();
            }


            //------------------------------------------
           
            int maxSum = -63;
            int currentSum = -63;

            for (int rw = 0; rw < rows - 2; rw++)
            {
                for (int cl = 0; cl < columns - 2; cl++)
                {
                    currentSum = arr[rw, cl] + arr[rw, cl + 1]
                    + arr[rw, cl + 2] + arr[rw + 1, cl + 1]
                    + arr[rw + 2, cl] + arr[rw + 2, cl + 1]
                    + arr[rw + 2, cl + 2];

                    Console.WriteLine("Current sum: " + currentSum);

                    if (currentSum > maxSum)
                        maxSum = currentSum;

                }
            }

            Console.WriteLine("Greatest sum: " + maxSum);

            Console.WriteLine(rows);
            Console.WriteLine(columns);

            Console.ReadLine();
        }
    }
}
