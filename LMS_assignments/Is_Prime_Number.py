''' Task : Write a program that takes a number from the user and prints the result to check if it is a prime number.

The examples of the desired output are as follows:

input →  19 ⇉ output : 19 is a prime number
input →  10 ⇉ output : 10 is not a prime number

The definition of a prime number is a positive integer that has exactly two positive divisors. 
1 only has one positive divisor (1 itself), so it is not prime. '''

num = int(input("Enter a number: "))  
  
if num > 1:  
   for i in range(2, num):  
       if (num % i) == 0:  
           print(num, "is not a prime number")  
           print(f"Because we can divide {num} by {i}.")  
           break  
   else:  
       print(num, "is a prime number")  
         
else:  
   print(num, "is not a prime number")  
   