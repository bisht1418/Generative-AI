# Problem 7: Iterate both lists simultaneously
list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]

for x in list1:
    for y in reversed(list2):
        print(f"{x} {y}")
        list2.pop()
        break
