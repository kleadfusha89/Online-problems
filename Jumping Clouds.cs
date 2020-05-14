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

class Solution
{

    // Complete the repeatedString function below.
    static long repeatedString(string s, long n)
    {
        long rem = n % s.Length;
        long repeated = n / s.Length;

        int occur = 0;
        long total;

        for (int i = 0; i < s.Length; i++)
        {
            if (s[i] == 'a')
                occur++;
        }

        total = occur * repeated;

        if (rem != 0)
        {
            for (int j = 0; j < rem; j++)
            {
                if (s[j] == 'a')
                    occur++;
            }
        }
        total += occur;

        return total;


    }

    static void Main(string[] args)
    {
        TextWriter textWriter = new StreamWriter(@System.Environment.GetEnvironmentVariable("OUTPUT_PATH"), true);

        string s = Console.ReadLine();

        long n = Convert.ToInt64(Console.ReadLine());

        long result = repeatedString(s, n);

        textWriter.WriteLine(result);

        textWriter.Flush();
        textWriter.Close();
    }
}
