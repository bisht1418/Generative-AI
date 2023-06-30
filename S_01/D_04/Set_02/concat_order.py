# Problem 6: Concatenate two lists in the following order
list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
ansList = []

for x in range(0, len(list1)):
    for y in range(0, len(list2)):
        bag = ""
        bag += list1[x]+" "+list2[y]
        ansList.append(bag)
print(ansList)
