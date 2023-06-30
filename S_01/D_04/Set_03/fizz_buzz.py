# FizzBuzz: Write a Python program that prints the numbers from 1 to 100, but for multiples of three, print "Fizz" instead of the number, for multiples of five, print "Buzz", and for multiples of both three and five, print "FizzBuzz".

bag = ""
for x in range(1, 101):
    if x % 3 == 0 and x % 5 == 0:
        bag += "FizzBuzz"
    elif x % 3 == 0:
        bag += "Fizz"
    elif x % 5 == 0:
        bag += "Buzz"
    else:
        bag += str(x)
    bag += ", "
print(bag)
