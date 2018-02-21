// Decompiled with JetBrains decompiler
// Type: flagbuilder.Program
// Assembly: flagbuilder, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null
// MVID: B1D8E7A6-CCA3-48AE-A08B-74EAA35ADCED
// Assembly location: C:\Users\Manzel\Desktop\flagbuilder.exe

using System;
using System.Text;

namespace flagbuilder
{
  internal static class Program
  {
    [STAThread]
    private static void Main()
    {
      Random random = new Random(239463551);
      StringBuilder stringBuilder = new StringBuilder();
      stringBuilder.Append("easyctf{");
      for (int index = 0; index < 6; ++index)
        stringBuilder.Append(random.Next());
      stringBuilder.Append("}");
      stringBuilder.ToString();
      Console.WriteLine("Flag created!");
    }
  }
}
