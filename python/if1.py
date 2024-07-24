'''find the greatest number entered by the user
a=int(input("type your digit1 : "))
b=int(input("type your digit2 : "))
c=int(input("type your digit3 : "))
d=int(input("type your digit4 : "))
if(a>c):
    f1=a
else:
    f1=c
if(b>d):
    f2=b
else:
    f2=d
if(f1>f2):
    print(str(f1) + "is the greatest digit")
else:
     print(str(f2) + "is the greatest digit")
'''
#find the smalest number
a=int(input("type your digit1 : "))
b=int(input("type your digit2 : "))
c=int(input("type your digit3 : "))
d=int(input("type your digit4 : "))
e=int(input("type your digit4 : "))
if(a<c):
    f1=a
else:
    f1=c
if(b<d):
    f2=b
else:
    f2=d
if(f1<e):
    f3=f1
else:
    f3=e
if(f1<e):
    f3=f1
else:
    f3=e
if(f3<f2):
    print(str(f3) + "is the smalest digit")
else:
     print(str(f2) + "is the smalest digit")