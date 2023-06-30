# 1. **Tuple Unpacking**: Create a list of tuples, each containing a name and an age. Then, use tuple unpacking to iterate through the list and print each name and age.

input = [("John", 25), ("Jane", 30)]
bag = ""
for x in input:
    bag += f"{x[0]} is {x[1]} years old."
print(bag)
