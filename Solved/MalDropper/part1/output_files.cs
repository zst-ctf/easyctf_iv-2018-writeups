using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Reflection;
using System.Text;


namespace ConsoleApp1
{
    class Program
    {
        private static bool CompareOffset(byte[] arr, int off, byte[] pattern)
        {
            for (int index = 0; index < pattern.Length; ++index)
            {
                if ((int)arr[off + index] != (int)pattern[index])
                    return false;
            }
            return true;
        }

        private static byte[][] SplitByteArray(byte[] arr, byte[] splitPattern)
        {
            int count = 0;
            List<byte[]> numArrayList = new List<byte[]>();
            for (int off = 0; off < arr.Length - splitPattern.Length; ++off)
            {
                if (Program.CompareOffset(arr, off, splitPattern))
                {
                    numArrayList.Add(((IEnumerable<byte>)arr).Skip<byte>(count).Take<byte>(off - count).ToArray<byte>());
                    count = off + splitPattern.Length;
                    off += splitPattern.Length - 1;
                }
            }
            numArrayList.Add(((IEnumerable<byte>)arr).Skip<byte>(count).ToArray<byte>());
            return numArrayList.ToArray();
        }

        static void Main(string[] args)
        {
            Console.Write("Enter maldropper.exe location: ");
            string location = Console.ReadLine();

            byte[][] numArray = Program.SplitByteArray(File.ReadAllBytes(location), Encoding.ASCII.GetBytes("[SPLIT" + "ERATOR]"));
            List<string> stringList = new List<string>();
            for (int index = 0; index < numArray[2].Length; ++index)
                stringList.Add(numArray[2][index].ToString());

            // Write out to file
            string dirname = Path.GetDirectoryName(location) + "\\";
            Console.WriteLine("Output files to: " + dirname);
            File.WriteAllBytes(dirname + "payload.exe", numArray[1]);
            File.WriteAllBytes(dirname + "param.gz", numArray[2]);
        }

    }
}
