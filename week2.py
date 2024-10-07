# If-else statements
a = int(input(" enter you age"))
print("your age is so", a)
# condtional opreators
#  > ,< ,<=, >=, ==, !=
if (a>18):
  print("you can vote")
else :
  print("you can't vote")
print(a<=18)
print(a>=18)
print(a==18)
print(a<18)
print(a>18)



#elif satement
num = int(input("enter the value :"))
if (num > 0):# e
  print("The num is positive integer")
elif(num==0):
  print(" The num is zero")
else:
  print("The num is negative integer")



# nested if statement
num = int(input(" Enter the value:"))
if (num < 10):
    print("The value is less than 10")
elif (num > 0):
  if (num <= 10):
      print("The value is between 0 to 10")
  elif (num >= 10 and num <= 100):
      print("The value is between 10 to 100")
  elif (num > 100):
      print("The value is greater than 100")
else:
    print("The value is zero")

  # Ex - 2
 import time

t = time.strftime('%H,%M,%S')
hour = int(time.strftime('%H'))
hour = int(input("Enter the time"))
print("hour")
if (hour > 0 and hour < 12):
     print("Good moring Sir")
elif (hour >= 12 and hour < 17):
    print("Good aftenoon sir")
elif (hour >= 17 and hour < 0):
     print("Good night sir")


# match case
x = int(input("Enter the value:"))
match x:
  case 0:
    print('x is zero')
  case 4 if x % 2 ==0:
    print("x % 2 ==0 and case is 4")
  case _ if x <10:
    print("x is less thn 10")
  case _ if x!=100:
    print( "x is not 100")
  case _:
    print(x)

# for loops
name = "Aditya"
for i in name :
  print(i,'-')

name = ["adeey","cbum","notvedant"]
for name in name:
  print(name)
  for i in name:
    print(i,"jod")

for a in range (21):
  print(a)
for b in range(2,7):
  print(b)

# while loops
a = int(input("enter the number"))
while(a<18):
  a = int(input("enter the number:"))
  print(a)
print("Done the loop")



# decreament while loop
a = int(input("enter the value:"))
while(a > 0):
  print(a)
  a = a - 1
else:
  print("ERROR")


# OUTPUTS
# A -
# d -
# i -
# t -
# y -
# a -
# adeey
# a jod
# d jod
# e jod
# e jod
# y jod
# cbum
# c jod
# b jod
# u jod
# m jod
# notvedant
# n jod
# o jod
# t jod
# v jod
# e jod
# d jod
# a jod
# n jod
# t jod
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
# 11
# 12
# 13
# 14
# 15
# 16
# 17
# 18
# 19
# 20
# 2
# 3
# 4
# 5
# 6
# enter the number 12
# enter the number:2
# 2
# enter the number:5
# 5
# enter the number:19
# 19
# Done the loop
#enter the value: 3
# 3
# 2
# 1
# ERROR
