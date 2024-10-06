print("Gaanpati bappa mourya")

#Variables and datatypes
# variable is container that holds data
# Data type is specific type of value a variable holds
a = 5
b ="Adeey"
c = True
d = 7.7
e = complex(8,3)
print()
print("the type of a is",type(a))
print("the type of b is",type(b))
print("the type of c is",type(c))
print("the type of d is",type(d))
print("the type of e is",type(e))



# Ex - 1
a= int(input("enter first number"))
b= int(input("enter secound number"))
# Assignment opreators
print("sum of two numbers is ",a+b)
print("sub of two numbers is ",a-b)
print("muptiplicaton of two numbers is ",a*b)
print("division of two numbers is ",a/b)



# type casting
#conversion of one datatype to other data type is type casting
# explict type casting
string = " 1"
num = 7
string_number = int( string)
sum = num + string_number
print(" the sum of both num is:",sum)

#implicit type casting
a = 3  #type of a is int
b = 30.14 # tupe of b is float
print(a+b) #So teh type of sum is float


# user input
a = input("enter 1st num")
b = input("enter 2nd num")
print(int(a)**int(b))




#for loop
name = "Cbum Bhai  "
for i in name:
  print(i )

  # string slicing
  name = "Aditya,bhai"
  print(name[0:9])  # for slicing square bracketare used
  lee = len(name)
  print(lee)
  print(name[3:9])
  print(name[:])
  print(name[:len(name) - 4])

  nm = "Harry"
  print(nm[-4:-2])




#string method
a = "!!Gover nment!!"
print(len(a))  #strings are inmuteable
print(a.upper())
print(a.lower())
print(a.rstrip("!"))
print(a.replace("Government","Adeey"))
print(a.split(" "))

b = "cbuM cbuM W"  #capitalize first character of string to upper case and rest all characters into lower case
print(b.capitalize())
print(b.count("cbuM"))

c = "welcome to the jurrasic park @@"
print(c.endswith("@@"))
print(c.islower())
print(c.isspace())
print(c.title())

d = "Cbumisverynaughtyboiandheisalsoveryskinny07"
print(d.find("is"))
print(d.index("very"))
print(d.isalnum())# A-Z , a-z ,0-9
print(d.isalpha())#A-Z ,a-z
print(d.isprintable())
print(d.swapcase())# swaps upper to lower case

##Output

# Gaanpati bappa mourya
# the type of a is <class 'int'>
# the type of b is <class 'str'>
# the type of c is <class 'bool'>
# the type of d is <class 'float'>
# the type of e is <class 'complex'>
# enter first number 34
# enter secound number 445
# sum of two numbers is  479
# sub of two numbers is  -411
# muptiplicaton of two numbers is  15130
# division of two numbers is  0.07640449438202247
#  the sum of both num is: 8
# 33.14
# enter 1st num 34
# enter 2nd num 56
# 57918773205287127842044254126179599852840968492056164062843692360166371779746690236416
# C
# Aditya,bh
# 11
# tya,bh
# Aditya,bhai
# Aditya,
# ar
# 15
# !!GOVER NMENT!!
# !!gover nment!!
# !!Gover nment
# !!Gover nment!!
# ['!!Gover', 'nment!!']
# Cbum cbum w
# 2
# True
# True
# False
# Welcome To The Jurrasic Park @@
# 4
# 6
# True
# False
# True
# cBUMISVERYNAUGHTYBOIANDHEISALSOVERYSKINNY07




