# Two Sum Problem: Given an array of integers and a target integer, find the two integers in the array that sum to the target.

list = [2, 7, 11, 15]
target = 9

for x in range(0, len(list)):
    sum = 0
    for y in range(x, len(list)):
        sum += list[y]

        if sum == target:
            print([x, y])
