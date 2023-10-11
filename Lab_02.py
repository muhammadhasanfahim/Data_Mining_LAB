# Recursive Function
def mur(k):
  if(k>0):
    result =k + mur(k-1)
    print(result)
  else:
    result =0
  return result

mur(6)

# sum of odd and even numbers from a set of numbers
list = input("Enter a list with space: ").split()

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

# find the smallest number from a set of numbers
list = input("Enter a list with space: ").split()
print("The original list is : " + str(list))

for i in range(0, len(list)):
    for j in range(i+1, len(list)):
        if list[i] >= list[j]:
            list[i], list[j] = list[j],list[i]

print(list[0])

# find the sum of all numbers between 50 and 100, which are divisible by 3 and not divisible by 5
sum=0
for i in range(50, 100):
  if(i%3==0 and i%5!=0):
    sum+=i

print(sum)

# find the second highest number from a set of numbers
list = input("Enter a list with space: ").split()
print("The original list is : " + str(list))

for i in range(0, len(list)):
    for j in range(i+1, len(list)):
        if list[i] <= list[j]:
            list[i], list[j] = list[j],list[i]

print(list[1])

# find the factorial of a number using for loop
n = int(input("Enter a number: "))
fact=1
for i in range(1, n+1):
    fact = fact * i

print(fact)

# generate Fibonacci series
n = int(input("Enter a number: "))
n1=0
n2=1
for i in range(n):
    if(i==0):
      print(i)
      print(1)
    else:
      print(n1+n2)
      temp=n1
      n1=n2
      n2=temp+n2

# largest number between two numbers using function
def func(n1,n2):
  if(n1>n2):
    return n1
  else:
    return n2

n=int(input("enter one numebr: "))
n1=int(input("enter another numebr: "))

print("LArgerst number is: ", func(n,n1))

# Write a python program to find the sum of the numbers passed as parameters
def sum(x):
    sum = 0
    for i in str(x):
        sum=sum+int(i)
        x = sum
    return x
number = int(input("Enter numbers: "))
result = sum(number)
print("Summation of numbers is:", result)