# in this program we made variable total function analyze number 

def analyze_numbers(n):
    # set to 0 is imp else trash value
    total = 0 
    for i in range(1, n + 1): # loop with  range n+ 1 increases the n by 1 it goes like 
        # 0+1 = 1 1+1 = 0 and so on this is the logic
        total += i 
    print("Sum from 1 to", n, ":", total)
    even_count = 0
    for i in range(1, n + 1): # similarly set the range 
        if i % 2 == 0: # if condtion statement used if remiander = 0 then it is even
            # logic 2/2 = 0 remiander but 3/2= 1 so uneven that is why the logic is correct
            even_count += 1
    print("Even numbers count:", even_count)

    largest_div3 = 0 # set var to 0 
    for i in range(1, n + 1): 
        if i % 3 == 0: # as the modulus gives remiander we use it as if the number is div by 3 it is 0
            largest_div3 = i
    print("Largest number divisible by 3:", largest_div3)


def print_numbers(n): # for this program fib numbers are third num = first + second
    # 0 + 1 = 1 and 1 + 1 = 2 that is why we need to change the a as b b as c as logic
    fib = []
    a = 0
    b = 1
    for i in range(n):
        fib.append(a)
        c = a + b
        a = b
        b = c
    print("Fibonacci series:", fib)

    even_count = 0 # same logic if the num is even remainder must be 0 
    for num in fib:
        if num % 2 == 0:
            even_count += 1
    print("Even numbers in series:", even_count)

    largest_multiple = None # base case is not 0 and remaidner 0 it is 
    # the largest number else it's not as if it's less than 0 it will not be higher automatically
    for num in fib:
        if num != 0 and num % n == 0:
            largest_multiple = num
    if largest_multiple is None:
        print("No multiple of", n, "found in the series")
    else:
        print("Largest multiple of", n, "in series:", largest_multiple)

    total = 0 # logic is adding all the number in simulatenously we can get total
    for num in fib:
        total += num
    print("Sum of the series:", total)

    if total > 200: # using operator > if total is greater than 200 it will print following else it will print the else statement
        print("The sum is greater than 200")
    else:
        print("The sum is not greater than 200")


# function calls to show both base case and other case
analyze_numbers(10)

print("\n--- Case where multiple exists ---")
print_numbers(1)

print("\n--- Case where multiple does not exist ---")
print_numbers(4)