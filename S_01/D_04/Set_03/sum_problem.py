# Two Sum Problem: Given an array of integers and a target integer, find the two integers in the array that sum to the target.

list = [2, 7, 11, 15]
target = 9

for x in range(0, len(list)):
    sum = 0
    for y in range(x, len(list)):
        sum += list[y]

        if sum == target:
            print([x, y])


# ==================================================
# GPT solution

# def two_sum(nums, target):
#     num_map = {}  # HashMap to store values and indices

#     for i, num in enumerate(nums):
#         complement = target - num
#         if complement in num_map:
#             return [num_map[complement], i]
#         num_map[num] = i

#     return []


# # Example usage:
# nums = [2, 7, 11, 15]
# target = 9
# result = two_sum(nums, target)
# print(result)
