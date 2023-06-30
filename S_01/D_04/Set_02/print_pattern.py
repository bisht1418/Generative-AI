# Problem 1: Print the following pattern

num = 6
for x in range(1, num+1):
    bag = ""
    for y in range(1, x):
        bag += str(y) + " "
    print(bag)
