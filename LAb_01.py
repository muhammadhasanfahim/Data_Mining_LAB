# printing Massage
print("Hello world!")
msg = "Hello world!"
print(msg)

# Concatening
first_name = "albert"
last_name = "einstein"
full_name = first_name + " " + last_name
print(full_name)

# Concatening
first_name = input("Enter first name")
last_name = input("Enter last Name")

print(first_name+' '+last_name)

# computes the value of n + nn + nnn
n=input("Enter a number n: ")

t1=int(n)*int(n)
t2=int(n)*int(n)*int(n)
comp=int(n)+int(t1)+int(t2)
print("The value is:",comp)

# Circle area
radius = int(input("Enter Radius "))
print("Area is: ",3.1416* (radius*radius))

# Even Or Odd
num=int(input("enter number"))
if(num % 2)==0:
    print("given number is even")
else:
  print("given is odd")


# Generate List From Comma Separated Numbers
values = input("Input some comma seprated numbers : ")
list = values.split(",")

print("List : ",list)

# Displaying First And LAst number from list
color_List = ["Red","Green","White" ,"Black"]
print( "%s %s"%(color_List[0],color_List[-1]))

# LArgest Among THree numbers
a=int(input("enter first number"))
b=int(input("enter seond number"))
c=int(input("enter third number"))

if a>b & a>c:
  print("a is the largest")
elif b>a & b>c:
  print("b is the largest")
else:
  print("c is the largest")

# Find Grade From number
print("Enter Marks of 5 Subjects: ")
markOne = int(input())
markTwo = int(input())
markThree = int(input())
markFour = int(input())
markFive = int(input())

avg = (markOne+markTwo+markThree+markFour+markFive)/5

if avg>=91 and avg<=100:
    print("Your Grade is A1")
elif avg>=81 and avg<91:
    print("Your Grade is A2")
elif avg>=71 and avg<81:
    print("Your Grade is B1")
elif avg>=61 and avg<71:
    print("Your Grade is B2")
elif avg>=51 and avg<61:
    print("Your Grade is C1")
elif avg>=41 and avg<51:
    print("Your Grade is C2")
elif avg>=33 and avg<41:
    print("Your Grade is D")
elif avg>=21 and avg<33:
    print("Your Grade is E1")
elif avg>=0 and avg<21:
    print("Your Grade is E2")
else:
    print("Invalid Input!")

# Sum of three given numbers
def sum_thrice(x, y, z):

     sum = x + y + z

     if x == y == z:
      sum = sum * 3
     return sum


a=int(input("enter first number"))
b=int(input("enter seond number"))
c=int(input("enter third number"))

print(sum_thrice(a, b, c))
print(sum_thrice(a, b, c))

# Odd Even Sum From list of numbers
list = [345, 893, 1948, 34, 2346]

print("The original list is : " + str(list))

odd_sum = 0
even_sum = 0

for i in list:
		if int(i) % 2 == 0:
			even_sum += int(i)
		else:
			odd_sum += int(i)

print("Odd digit sum : " + str(odd_sum))
print("Even digit sum : " + str(even_sum))

# TRiangle is Valid or not
def triangle(a,b,c):
    if a+b>=c and b+c>=a and c+a>=b:
        return True
    else:
        return False

a = float(input('Enter length of side a: '))
b = float(input('Enter length of side b: '))
c = float(input('Enter length of side c: '))

if triangle(a, b, c):
    print('Triangle is Valid.')
else:
    print('Triangle is Invalid.')