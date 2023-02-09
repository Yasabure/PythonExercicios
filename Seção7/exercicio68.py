from operator import concat


def concat_letra_letra(str1: str, str2: str) -> str:
   str3 = ''
   if len(str1) > len(str2):
       for r in range(0, len(str1)):
           str3 += str1[r]
           if r < len(str2):
               str3+= str2[r]
       return str3
   else:
       for r in range(0, len(str2)):
           if r < len(str1):
               str3+= str1[r]
           str3 += str2[r]
       return str3



print(concat_letra_letra('135','24'))
    