string = input()
newstring = ''
flag = False
for i in string:
    flag = i.isdigit()
    if flag:
        continue
    else:
        newstring=newstring+i


string=newstring
print(string)
