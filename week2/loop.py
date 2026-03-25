# # ============================================
# # 1. FOR LOOP - Loop over a range
# # ============================================

# for i in range(50):
#     if i % 2 != 0:
#         print("Number:", i)
    
# # Output:
# # Number: 0
# # Number: 1
# # Number: 2
# # Number: 3
# # Number: 4
# n = int(input("Enter a number: "))
# for i in range(n):
#     if i > 0:
#         if i % 2 == 0:
#          print("Number:", i)

# n = int(input("Enter a number: "))
# for i in range(n+1):
#         mult = i * n 
#         if mult > 0:   
#             print("Number is", mult)
# n = int(input("Enter a num: "))
# sum=0
# for i in range(1, n+1):
#     sum= sum + i 
#     print(i, end=" ")
#     print("sum is", sum)

# n= int(input("Enter a number for factorial "))
# fact = 1
# for i in range(1, n+1):
#         fact = fact * i
#         print(fact)

# using while loop now  to get last num
# rev=0
# n = int(input("Enter a number "))
# while(n!=0):
#     rem=n%10
#     rev=rev*10+rem
#     n=n//10

# print("The number is", rev)
n = int(input("Enter a number: "))
a = 0
b = 1

if n <= 0:
    print("Enter a positive number")
else:
    for i in range(n):   # ✅ just range(n)
        c = a + b
        a = b
        b = c
    print("The result is", c)