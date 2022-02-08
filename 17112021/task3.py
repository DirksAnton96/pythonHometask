#try:
#  string = input()
#  string = string.strip(' ')
#  string = string.upper()
#  print(string)
#except:
#  print("Check what you type")


#variant2
string =" jgd gd5 "
i=0
s=""
for k in string:
    if (k==' ' and i==0) or (k==' ' and i==len(string)-1):
       i=i+1
      # string=string.replace(k, "")
      #  string=string.replace(k, "")
    else:
      i=i+1
      s=s+k
      
      
print(s)
print(len(s))
print("Hello")
