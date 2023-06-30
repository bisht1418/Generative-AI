# Problem 3: Append new string in the middle of a given string

s1 = "Ault"
s2 = "Kelly"

mid = len(s1) // 2
s1_length = len(s1)

startStr = s1[0:mid]
endStr = s1[mid:s1_length+1]

print(startStr+s2+endStr)
