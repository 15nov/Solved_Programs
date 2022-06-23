#Code for the word problem
s=str(input(''))
Y=0
Z=0
for i in range(0,len(s)):
    x=s[i].isupper()
    if x==False:
        Y+=1
    elif x==True:
        Z+=1
if Z>Y:
    p=s.upper()
    print(p)
elif Y>Z:
    p=s.lower()
    print(p)
else:
    p=s.lower()
    print(p)




