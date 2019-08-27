print("Enter the element to find all the divisors of it")
x = int(input())
i = 1
while i<x:
   if x%i == 0:
      print(i,"divisor")
   i = i + 1
