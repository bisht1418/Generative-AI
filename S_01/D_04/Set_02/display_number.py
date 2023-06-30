# Problem 2: Display numbers from a list using loop

numbers = [12, 75, 150, 180, 145, 525, 50]

for x in range(0, len(numbers)):
    if numbers[x] > 500:
        break
    elif numbers[x] > 150:
        continue
    elif numbers[x] % 5 == 0:
        print(numbers[x])
