# Insertion sort Algorithm
# Insertion sort Algorithm is Stable sorting Algorithm
# Insertion sort Algorithm is Adaptive Algorithm
# Time complexity of Insertion sorting Algorithm is O(n^2)
# Best case Time complexity O(n)

# Array for sorting
Array = [1, 3, 7, 91, 7]

for j in range(1, len(Array)):
    for i in range(j):
        if Array[j - i] <= Array[j - i - 1]:
            # Swape elements
            Array[j - i], Array[j - i - 1] = Array[j - i - 1], Array[j - i]

print("Sorted Array using Insertion sorting Algorithm")
print(Array)
