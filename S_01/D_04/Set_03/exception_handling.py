# Exception Handling: Write a Python function that takes two numbers as inputs and returns their division, handling any potential exceptions (like division by zero).

def num_division(a, b):
    if a % b == 0:
        return f"Divided by {b}"
    else:
        return f"Cannot divide by {b}."


print(num_division(10, 3))
