#string = "aa1234567+ls;lmd89s38fm"
string = input()
a=0
for char in string:
     if char == "8":
        a = int(a)+8
     elif char == "3":
        a = int(a)+3
     elif char == "1":
        a = int(a)+1
     elif char == "2":
        a = int(a)+2
     elif char == "4":
        a = int(a)+4
     elif char == "5":
        a = int(a)+5
     elif char == "6":
        a = int(a)+6
     elif char == "7":
        a = int(a)+7
     elif char == "0":
        a = int(a)+0
     elif char == "9":
        a = int(a)+9
     else:
        continue
print(a)
