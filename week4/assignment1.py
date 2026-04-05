def fibonacci(n):
    if n <= 0: # if else condition since fib is first term plus second term and so on
        return 0 
    elif n == 1:  # these condition is needed as first num should always be 0 and seocnd always 1 that is why base case is needed 
        # c = 0 + 1 , c = 1+1, c=2+1 main logic is first term + last term = result 
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

n = int(input("Enter how many terms: "))

for i in range(n):
    print(fibonacci(i), end=" ") # iteration is done until base case is meet