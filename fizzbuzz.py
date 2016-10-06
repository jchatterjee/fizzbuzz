import sys

for arg in sys.argv[1:]:
    n = int(arg)

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