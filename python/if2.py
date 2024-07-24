'''write a program where the pass marks required 40% and atleat 30% out of 700 
create 7subjects marks entered by user
and grade the marks accordingly
>90=EX
80~90=AA
70~80=A
60~70=B
50~60=C
40~50=D
30~40=E
<30=F'''
m=int(input("type your sub1 : "))
e=int(input("type your sub2 : "))
b=int(input("type your sub3 : "))
h=int(input("type your sub4 : "))
g=int(input("type your sub5 : "))
ph=int(input("type your sub6 : "))
ch=int(input("type your sub7 : "))
total=(m+e+b+h+g+ph+ch)/700
per=str(round(total*100))+ '%'
cri1=str(round((280/700)*100))+ '%'#D
cri2=str(round((210/700)*100))+ '%'#E
cri3=str(round((350/700)*100))+ '%'#C
cri4=str(round((420/700)*100))+ '%'#B
cri5=str(round((490/700)*100))+ '%'#A
cri6=str(round((560/700)*100))+ '%'#AA
cri7=str(round((630/700)*100))+ '%'#EX

if(per>cri1):
  print("pass")
elif(per>cri2):
  print("ok")
elif(per<cri2):
  print("fail")

if (per>=cri7):
    grade="EX"
elif(per>=cri6):
   str(grade="AA")
elif(per>=cri5):
   str(grade="A")
elif(per>=cri4):
   str(grade="B")
elif(per>=cri3):
   str(grade="C")
elif(per>=cri1):
   str(grade="D")
elif(per>=cri2):
   str(grade="E")
else:
   grade="F"