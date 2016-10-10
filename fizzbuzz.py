import sys

if sys.argv[1:]:
    for arg in sys.argv[1:]:
        user_n = arg
else:
    user_n = input("How high do you want to count? ")

while True: 
    try:
        n = int(user_n)
        if n > 0:
            break
        else:
            print("Please enter a positive integer.")
            user_n = input("How high do you want to count? ")
    except ValueError:
        print("Please enter a positive integer.")
        user_n = input("How high do you want to count? ")
        
x = 1

print("Fizz Buzz counting up to {}".format(n))

while x <= n:
    if x % 15 == 0:
        print("FizzBuzz")
    elif x % 3 == 0:
        print("Fizz")
    elif x % 5 == 0:
        print("Buzz")
    else:
        print(x)
    x += 1