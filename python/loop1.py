#write a sequence to 1~50 with while loop
'''i=0
while (i<50):
    i=i+1
    print(i)'''
#write a programme to 1~6 and skip 3
'''i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)#here the continoue statement has skip the value of i==3
'''
#write a program for making a sequence of 1~50 using for loop
'''for x in range(50):
    print(x)
'''
#1 write a table using for loop of given number 
for x in range(2,22,2):
 print(x)#in 1st digit states starting range 2nd digit states ending range 3rd digit states skip
num=int(input("type your digit:"))
for i  in range(1,11):
 print(str(num)+"X"+ str(i)+ "=" + str(num*i))
 #print(f"{num}X{i}={i*num}")

 '''fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)
  fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)#here break statement will stop this  loop
'''
