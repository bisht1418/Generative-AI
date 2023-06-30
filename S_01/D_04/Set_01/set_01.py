# Hello, World!: Write a Python program that prints "Hello, World!" to the console.
print("Hello, World!:")

# Create variables of each data type (integer, float, string, boolean, list, tuple, dictionary, set) and print their types and values.
integer = 10
print(integer)

string = "Hello! Masai :)"
print(string)

boolean = 10 > 20
print(boolean)

list = [1, 2, 3, 4, 5]
print(list)

tuple = (1, 2, 3, 4, 5)
print(tuple)

dictionary = {1: "a", 2: "b", 3: "c", 4: "d"}
print(dictionary)

set = {1, 2, 3, 4, 5}
print(set)


# List Operations: Write a Python program to create a list of numbers from 1 to 10, and then add a number, remove a number, and sort the list.
num = 1
my_list = []
while num <= 10:
    my_list.append(num)
    num += 1
print(my_list)

my_list.append(20)
print(my_list)

my_list.pop(3)
print(my_list)

my_list.sort()
print(my_list)


# Sum and Average: Write a Python program that calculates and prints the sum and average of a list of numbers.
my_input = [10, 20, 30, 40]
my_sum = 0
for sum in my_input:
    my_sum += sum
my_avg = my_sum / len(my_input)
print(f"Sum: {my_sum}, Average:{my_avg}")


# String Reversal: Write a Python function that takes a string and returns the string in reverse order.
def reverse_string(input_string):
    reversed_string = ""
    for char in input_string:
        reversed_string = char + reversed_string
        print(char)
    return reversed_string


my_input_string = "Python"
my_rev_input = reverse_string(my_input_string)
print(my_rev_input)


# Count Vowels: Write a Python program that counts the number of vowels in a given string.
def count_vowels(str):
    vowels = "aeiouAEIOU"
    count = 0
    for char in str:
        if char in vowels:
            count += 1
    return count


my_string = "Hello"
num_vowels = count_vowels(my_string)
print(num_vowels)


# Prime Number: Write a Python function that checks whether a given number is a prime number.
check_prime = 13
count = 0

for x in range(1, check_prime + 1):
    if check_prime % x == 0:
        count += 1

if count == 2:
    print(check_prime, "is a prime number")
else:
    print(check_prime, "is not a prime number")


# Factorial Calculation: Write a Python function that calculates the factorial of a number.
num_factorial = 5
factorial = 1

for x in range(1, num_factorial+1):
    factorial *= x
print(factorial)


# Fibonacci Sequence: Write a Python function that generates the first n numbers in the Fibonacci sequence.

def fibonacci_sequence(n):
    sequence = [0, 1]
    if n <= 2:
        return sequence[:n]

    while len(sequence) < n:
        next_number = sequence[-1] + sequence[-2]
        sequence.append(next_number)
    return sequence


n = 5
fib_sequence = fibonacci_sequence(n)
print(fib_sequence)


# List Comprehension: Use list comprehension to create a list of the squares of the numbers from 1 to 10.

square_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
ans_square = []

for x in range(1, 11):
    ans_square.append(x**2)
print(ans_square)
