using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Remove_Duplicates
{ 
    class Program
    {
        public static string remDuplicates(string str)
        {
            HashSet<char> mySet = new HashSet<char>();
            
            
            for(int i = 0; i < str.Length; i++)
            {
                mySet.Add(str[i]);
            }

            HashSet<char>.Enumerator em = mySet.GetEnumerator();
            string val = "";
            while (em.MoveNext())
            {
                val += em.Current;
            }


            return val;
        }
        static void Main(string[] args)
        {
            string str = "";
            Console.Write("Enter a string: ");
            str = Console.ReadLine();
            
            Console.WriteLine("Removed duplicates: " + remDuplicates(str));

            Console.Read();
        }
    }
}
