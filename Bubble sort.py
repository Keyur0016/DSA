# Bubble sort algorithm
# Bubble sort time complexity are O(n^2)
# Bubble sort work on comparison element by one by one

# Array for sorting
Array = [9, 1, 2, 4, 90, 16]

# Here total number passes are 5

for i in range(len(Array)):
    for j in range(len(Array) - i - 1):
        if Array[j] >= Array[j + 1]:
            Array[j], Array[j + 1] = Array[j + 1], Array[j]
        else:
            pass

print("Sorted array by Bubble sort Algorithm")
print(Array)

