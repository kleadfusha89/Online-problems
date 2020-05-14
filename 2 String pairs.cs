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

namespace _2_Strings_hashset
{
    class Program
    {
      


        static bool Check(string s1, string s2)
        {
            
            
            HashSet<char> str1 = new HashSet<char>();
            HashSet<char> str2 = new HashSet<char>();
            
            for (int i = 0; i < s1.Length; i++)
            {
                str1.Add(s1[i]);
            }

            for (int j = 0; j < s2.Length; j++)
            {
                str2.Add(s2[j]);
            }

            




            if (str1.Overlaps(str2))
                return true;
            else
                return false;
            
        }


        static int sockMerchant(int[] arr, int n)
        {
            int pairs = 0;


            HashSet<int> mySet = new HashSet<int>();
            

            for (int i = 0; i < n; i++)
            {
                if (!mySet.Contains(arr[i]))
                    mySet.Add(arr[i]);
                else
                {
                    pairs++;
                    mySet.Remove(arr[i]);
                }
            }

            
            return pairs;
        }

        static void Main(string[] args)
        {

            string s1 = "hbbo";
            string s2 = "aeer";

            Console.WriteLine(Check(s1, s2));
            

            //--------------------\\
            int[] arr = { 10, 10, 20, 20, 11, 14, 11, 14 };
            int n = arr.Length;

            Console.WriteLine(sockMerchant(arr, n));


            Console.Read();
        }
    }
}
