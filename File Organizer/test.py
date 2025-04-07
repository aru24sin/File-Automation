fileFound = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2]
target = 2
count = 0

for file in fileFound:
    if file == target:
        count += 1
    if count == 2:
        print("Found the target twice")
        