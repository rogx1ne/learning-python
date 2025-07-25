#wap to find if the no entered is prime or not if not then print the next prime no:


# def isprime(n):
#     if n<2:
#         return False
    
#     for i in range(2,int(n**0.5)+1):
#         if n%i==0:
#             return False
#         else:
#             continue
#     return True

# n=int(input("Enter a no: "))

# prime=isprime(n)
# if prime: print("prime")
# else:
#     print("it is not prime")
#     while (not prime):
#         n+=1
#         prime=isprime(n)
#         if prime:
#             print(n,"is next prime")

#--------------------------------------------------------------------------------------------------------------------------------------
 
# 1. What is the data type of 5.0 in Python?

#type(5.0)


# 2. How do you convert a string "123" to an integer?

# int("123")

# 3. What will type(True) return?

#<class 'bool'>

# 4. What happens when you add an integer to a string? Try: "5" + 5.

# >>> "5"+5
# Traceback (most recent call last):
#   File "<python-input-0>", line 1, in <module>
#     "5"+5
#     ~~~^~
# TypeError: can only concatenate str (not "int") to str
# >>> 


# 5. Write a Python program to input age and print its data type.

# age=input("Enter your age: ")
# type(age) #will print sting
# age=int(age)
# type(age) #will print integer

# 6. Define and print the length of a string input by the user.

# str=input("enter a string: ")
# c=0
# for i in str:
#     c+=1
# print("length: ",c)

# 7. What is the output of: type(3 + 4.5)?

#7.45

# 8. Input a number and convert it to a float.

# n=int(input("Enter a integer: "))
# n=float(n)

# 9. Write a program that accepts a string and prints its first and last character.

# name=input("enter your name: ")

# c=0
# for i in str:
#     c+=1

# print(name[0],name[c-1])
# print(name[0],name[-1])

# 10. Write a program to check if a variable is of type int or float.

# var="ghfj"
# if isinstance(var, int):
#     print("Integer")
# elif isinstance(var, float):
#     print("Float")
# else:
#     print("none of mentioned")

# 11. Write a program to check if a number is positive, negative, or zero.

# n=int(input("Enter a no: "))
# if n>0:
#     print("positive")
# elif n<0:
#     print("negative")
# else:
#     print("zero")


# 12. Ask user to enter age. If age >= 18, print "Eligible to vote", else print "Not eligible".

# age=int(input("Enter your age: "))
# if age>=18:
#     print("egligible to vote")
# else:
#     print("not eligible")


# 13. Input a number. If it is even, print "Even", else print "Odd".

# n=int(input("Enter a no: "))
# if(n%2==0):
#     print("even")
# else:
#     print("odd")


# 14. Write a program to find the greatest of 3 numbers.

# n1=int(input("Enter no1: "))
# n2=int(input("Enter no2: "))
# n3=int(input("Enter no3: "))
# if n1>n2 and n1>n3:
#     print("greatest no:",n1)
# elif n2>n3:
#     print("greatest no:",n2)
# else:
#     print("greatest no:",n3)

# 15. Check if a year is a leap year or not.

# year=int(input("Enter a year: "))
# if (year%4==0 and year%100!=0) or (year%400==0):
#     print("leap year")
# else:
#     print("not a leap year")
    
# 16. A student passes if marks >= 40. Print "Pass" or "Fail" based on input.

# marks=int(input("Enter your marks: "))
# if marks>=40:
#     print("pass")
# else:
#     print("fail")


# 17. If score >= 90 → A, 80–89 → B, 70–79 → C, else F. Write a grade calculator.

# score=int(input("Enter your score: "))
# if score>=90: print("A")
# elif 89>=score>=80: print("B")
# elif 79>=score>=70: print("C")
# else: print("F")


#18. Ask user for a number. If divisible by 3 and 5, print "FizzBuzz".

# n=int(input("enter a no: "))
# if n%3==0 and n%5==0:
#     print("FizzBUzz")


#19. Write a program that checks whether a character is a vowel or consonant.

# ch=input("Enter a character: ")

# if(ch=="a" or ch =="e" or ch=="i" or ch =="o" or ch=="u" or ch=='A' or ch =='E' or ch =='I' or ch=='O' or ch=='U'):
#     print("vowel")
# else: 
#     print("consonant")


# 20. Ask user to input temperature. If temp > 30, print "Hot", if < 15, print "Cold", else "Moderate".

# temp=int(input("Enter the temperature: "))
# if temp>30:print("Hot")
# elif temp<15:print("cold")
# else:print("moderate")


# 21. Write a for loop to print numbers from 1 to 10.

# for i in range(1,11):
#     print(i)
# i=1
# while(i<=10):
#     print(i)

# 22. Use a while loop to print even numbers from 2 to 20.

# i=2
# while(i<=20):
#     if(i%2==0):print(i,end=" ")
#     i+=2


#23. Print the multiplication table of a number entered by the user.

# n=int(input("Enter a no: "))
# for i in range(1,11):
#     print(n,"*",i,"=",n*i)


#24. Print the factorial of a number using a loop.

# n=int(input("Enter a no: "))
# f=1
# while(n>1):
#     f*=n
#     n-=1
# print("factorial : ",f)


# 25. Use a loop to find the sum of the first n natural numbers.

# n=int(input("Enter a no: "))
# s=0
# while(n>0):
#     s+=n
#     n-=1
# print("sum of n natural nos: ",s)




# 26. Write a loop to find the sum of digits of a number.

# n=input("enter a no: ")
# sum=0
# for i in n:
#     sum+=int(i)
# print(sum)


#27. Print all the odd numbers between 1 to 50.

# for i in range(1,50):
#     if i%2!=0: print(i,end=" ")


#28. Use a loop to reverse a string entered by the user.

# str=input("Ener a string: ")
# rev=""
# for i in str:
#     rev= i+ rev
# print(rev)


# 29. Count how many vowels are present in a given string.

# str=input("enter a string: ")
# v=0
# for ch in str:
#     if(ch=="a" or ch =="e" or ch=="i" or ch =="o" or ch=="u" or ch=='A' or ch =='E' or ch =='I' or ch=='O' or ch=='U'):
#         v+=1
# print("vowel present: ",v)


#30. Generate Fibonacci series up to n terms using loop.

# n1,n2=0,1
# n=int(input("Enter the value of n: "))
# for i in range(n):
#     print(n1)
#     n1,n2=n2,n1+n2

#31. Write a program to check whether a number is prime using loop.

# n=int(input("Enter a no: "))


# if n<2:
#     print("not prime")
    
# for i in range(2,int(n**0.5)+1):
#     if n%i==0:

#         print("not prime")
#         break
#     else:
#         continue
#     print("prime")


# 32. Print numbers from 1 to 100. If the number is divisible by 3, print “Fizz”; if by 5, print “Buzz”; if by both, print “FizzBuzz”.

# for i in range(1,101):
#     if i%3==0 and i%5==0:print(i,"FizzBuzz")
#     elif i%3==0:print(i,"Fizz")
#     elif i%5==0:print(i,"Buzz")
#     else: print(i)


# 33. Print a pattern like:
# *
# **
# ***
# ****


# for i in range(5):
#     for j in range(i):
#         print("*",end="")
#     print()


#34. Write a loop to display all characters of a string with their index.

# str=input("Enter a string: ")
# for i in range(len(str)):
#     print(str[i],i)

# 35. Ask the user to input a number and print the square of each number from 1 to that number.

# n=int(input("Enter a no: "))
# for i in range(1,n+1):
#     print("sqr of",i,":",i*i)

# 36. Use nested if to print grades:
# - >90: A+
# - >75: A
# - >60: B
# - Else: Fail

# marks=int(input("Enter marks: "))
# if marks>60:
#     if marks>75:
#         if marks>90: print("A+")
#         else: print("A")
#     else: print("B")
# else:print("fail")

# 38 Create a loop that accepts 5 numbers from the user and prints their average.

# s=0
# for i in range(5):
#     n=int(input("Enter a no: "))
#     s+=n
# print("avg sum: ",s/5)

# 39. Write a program to find the largest of three numbers using nested if.

# n1=int(input("Enter no1: "))
# n2=int(input("Enter no2: "))
# n3=int(input("Enter no3: "))
# if n1>n2:
#     if n1>n3:print(n1)
#     else:print(n3)
# elif n2>n3:print(n2)
# else:print(n3)


#40. Write a loop that skips numbers divisible by 3 using continue.

# for i in range(10):
#     if i%3==0:continue
#     else:print(i)


# 41. Write a program that takes a number and prints if it is prime or not using nested for loop.

# num = int(input("Enter a number: "))
# is_prime = True
# if num <= 1:
#     is_prime = False
#     print(f"{num} is not a prime number")
# else:
#     for i in range(2, num):
#             if num % i == 0:
#                 is_prime = False
#                 print(f"{num} is divisible by {i}")
#                 break
#         if not is_prime:
#             break
#     if is_prime:
#         print(f"{num} is a PRIME number!")
#     else:
#         print(f"{num} is NOT a prime number.")


# 42. Take 5 inputs and count how many are positive.

# c=0
# for i in range(5):
#     n=int(input("Enter a no: "))
#     if n>0: c+=1
# print("positive nos: ",c)


# 43. Accept a string and count the number of uppercase and lowercase letters.

# str=input("Enter a string: ")
# uc=lc=0
# for ch in str:
#     if 65<=ord(ch)<=90:uc+=1
#     elif 97<=ord(ch)<=122:lc+=1
# print("uppercase: ",uc,"\nlowercase: ",lc)


#44. Create a login system: if username and password match, print success, else retry 3 times.

# correct_pin="adcv"
# pswd="1245"
# attempts = 0
# print("login")
# while attempts < 3:
#     user_pin = input("Enter your username: ")
#     user_pswd = input("Enter your password: ")
#     if user_pin == correct_pin or user_pswd==pswd:
#         print("You are loggged in")
#         break  
#     else:      
#         attempts +=1
#         if attempts < 3:
#             remaining = 3 - attempts
#             print("Wrong username or password You have", remaining, "attempts left")
#         else:
#             print("Wrong username or password entered 3 times!")
            

# 45. Print reverse of a number using while loop.

# n=int(input("Enter a no: "))
# while(n>0):
#     print(n%10,end="")
#     n//=10

# 46. Print all numbers from 1 to 50, but break the loop if number reaches 25.
# for i in range(1,51):
#     print(i)
#     if i==25:
#         break

# 47. Ask the user to enter a number. Use a loop to check whether it is a palindrome number.
12


# 48. Find the sum of all numbers between 1 to 100 that are divisible by 9.

# s=0
# for i in range(1,100):
#     if i%9==0:s+=i 
# print(s)


# 49. Use a loop to print all characters in a string that are not vowels.

# str=input("Enter a string: ")
# for ch in str:
#         if(ch=="a" or ch =="e" or ch=="i" or ch =="o" or ch=="u" or ch=='A' or ch =='E' or ch =='I' or ch=='O' or ch=='U'):
#             continue
#         else:
#             print(ch,end="")
# print()


# 50. Write a program to input 3 numbers and print the second largest using if statements.

# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# num3 = int(input("Enter third number: "))
# if num1 >= num2 and num1 >= num3:
#     if num2 >= num3:
#         second_largest = num2
#     else:
#         second_largest = num3
# elif num2 >= num1 and num2 >= num3:
#     if num1 >= num3:
#         second_largest = num1
#     else:
#         second_largest = num3
# else:
#     if num1 >= num2:
#         second_largest = num1
#     else:
#         second_largest = num2
# print(f"The second largest number is: {second_largest}")



# 51.forgot password (in this I have not made it like after it changes the password it will re-enter the user name I have made it like a normal one to reset the password, in future I may update it)

# usrnm="adcv"
# pswd="1245"
# attempts = 0
# print("login")
# while attempts < 3:
#     user_pin = input("Enter your username: ")
#     user_pswd = input("Enter your password: ")
#     if user_pin == usrnm and user_pswd==pswd:
#         print("You are loggged in")
#         break  
#     else:      
#         attempts +=1
#         if attempts < 3:
#             remaining = 3 - attempts
#             print("Wrong username or password You have", remaining, "attempts left")
#         else:
#             print("Wrong username or password entered 3 times!")
#             ch=input("Do u want to reset the password (y/n): ")
#             if ch=='y' or ch=='Y':
#                 rpswd=input("enter the new password: ")
#                 rentr=input("renter the new password: ")
#                 if rpswd==rentr:
#                     pswd=rpswd
#                     print("password reset success!")
#                 else:
#                     print("rentered password does not match the new password")
