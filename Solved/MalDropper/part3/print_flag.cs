using System;
using System.Text;

namespace printflag
{
  static class Program
  {
    static void Main()
    {
      Random random = new Random(239463551);
      StringBuilder stringBuilder = new StringBuilder();
      stringBuilder.Append("easyctf{");
      for (int index = 0; index < 6; ++index)
        stringBuilder.Append(random.Next());
      stringBuilder.Append("}");
      stringBuilder.ToString();
      Console.WriteLine("Flag is: " + stringBuilder.ToString());
    }
  }
}
