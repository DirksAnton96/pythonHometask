pharse = "Don't panic!"
plist = list(pharse)
print(pharse)
print(plist)
new_pharse=''.join(plist[1:3:1])
new_pharse=new_pharse+''.join([plist[5],plist[4],plist[7],plist[6]])
print(plist)
print(new_pharse)