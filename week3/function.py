# def odd_even(num):
#     if num % 2==0:
#         print("even")
#     else:
#         print("odd")


# odd_even(6)
# // wap to find hcf and lcf using py
def hcf(a, b):
    while b != 0:
        a, b = b, a % b  
        # 12, 18 = 18, 6
    return a
# 108 // 18 , 6 
def lcm(a, b):
    return (a * b) // hcf(a, b)

num1 = 12
num2 = 18

print("HCF:", hcf(num1, num2))
print("LCM:", lcm(num1, num2))
     