using System.CodeDom.Compiler;
using System.Collections.Generic;
using System.Collections;
using System.ComponentModel;
using System.Diagnostics.CodeAnalysis;
using System.Globalization;
using System.IO;
using System.Linq;
using System.Reflection;
using System.Runtime.Serialization;
using System.Text.RegularExpressions;
using System.Text;
using System;

namespace special_substring
{
    class Program
    {
        static int countInt(int special)
        {
            int sum = 0;
            for(int i = 1; i < special; i++)
            {
                sum += i;
            }
            return sum;
        }


        static int subSpecial(string s, int n)
        {
            if (n == 0 || n == 1 || n == 2)
                return n;


            int result = 0;
            int special = 1;

            int specialBothWays = 0;
            int SpecialBothWaysIndex = 1;
            
            

            for (int i = 1; i < n; i++)
            {
                if(s[i - 1] == s[i])
                {
                    special++;

                }
                else
                {

                    result += countInt(special);
                    Console.WriteLine("After countIntSpecial    " + result);

                    while (SpecialBothWaysIndex < n - i)
                    {
                        if (s[i - SpecialBothWaysIndex] != s[i + SpecialBothWaysIndex])
                            break;
                        if (s[i] == s[i - 1] || s[i] == s[i + 1])
                            break;
                        specialBothWays++;
                        SpecialBothWaysIndex++;
                    }


                    result += specialBothWays;
                    Console.WriteLine("After specialBothWays   " + result);


                    special = 1;
                }
            }

            if (special > 1)
            { 
                result += countInt(special);
                Console.WriteLine("After if(special>1)     " + result);

            }

            result += n;
            Console.WriteLine("After += n    " + result);




            return result;
        }

        static void Main(string[] args)
        {

            //string s = Console.ReadLine();
            string s = "aaaabaaaa";
            int n = s.Length;


            Console.WriteLine(subSpecial(s, n));

            









            Console.Read();
        }
    }
}
