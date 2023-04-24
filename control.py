#simple if
n=10
if(n %2==0):
    print("n is an even number")

    #if_else
    n=5
    if(n % 2==0):
        print("n is even")
    else:
        print("n is odd")

        #nested if statement which is if statement that is inside another if statement
        a=5
        b=10
        c=15
        if a >b:
            if a>c:
                print("a value is big")
            else:
                print("c value is big")
        elif b>c:
            print("b value is big")
        else:
            print("c is big")

 #Given the nested if-else structure below, what will be the value of x 
 #  #after code execution completes
x = 0
a = 0
b = -5
if a > 0:
    if b < 0: 
        x = x + 5 
    elif a > 5:
        x = x + 4
    else:
        x = x + 3
else:
    x = x + 2
print(x)

 #What is the output of the following nested loop

numbers = [10, 20]
items = ["Chair", "Table"]

for x in numbers:
  for y in items:
    print(x, y)

# What is the output of the following nested loop?

for num in range(10, 14):
   for i in range(2, num):
       if num%i == 1:
          print(num)
          break
       
       #Write a program that prints the numbers from 1 to 100.
       #But for multiples of three print “Fizz” instead of the 
       #number and for the multiples of five print “Buzz”. For numbers
       #which are multiples of both three and five print “FizzBuzz”.

for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)

#Write a function that takes a list of integers as input and prints 
#the sum of all the even numbers in the list.
# nums=[1,2,3,14,12,10,16]
# def even_numbers(*nums):
#     sum=0
#     for i in nums:
#         if i %2==0:
#             sum+=i
#             print (sum)

# def sum_even(a, b):
#     count = 0
#     for i in range(a, b, 1):
#         if(i % 2 == 0):
#             count += [i]
#         return count
#     print(count)

