string = input()
#newstring = ''
flag = False
for i in string:
    flag = i.isdigit()
    if flag:
       # continue
        string=string.replace(i,"")
    else:
        continue
#        newstring=newstring+i
       


#string=newstring
print(string)
