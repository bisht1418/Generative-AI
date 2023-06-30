# Problem **5: Concatenate two lists index-wise**

list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]

ansList = []

for x in range(0, len(list1)):
    bag = ""
    bag += list1[x]+list2[x]
    ansList.append(bag)
print(ansList)
