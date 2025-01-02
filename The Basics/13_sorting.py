# selection sort
num = [5, 2, 8, 1, 9]

for i in range(len(num)):
    min_index = i
    for j in range(i + 1, len(num)):
        if num[j] < num[min_index]:
            min_index = j
    num[i], num[min_index] = num[min_index], num[i]
print(num)

# bubble sort
arr = [64, 34, 25, 12, 22, 11, 90]

n = len(arr)

# Outer loop for the number of passes
for i in range(n):
    swapped = False  # To track if any swapping happens
    # Inner loop to compare and swap elements
    for j in range(0, n - i - 1):
        if arr[j] > arr[j + 1]:
            # Swap the elements
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            swapped = True
    # If no swapping happens, the list is already sorted
    if not swapped:
        break

# Print the sorted array
print("Sorted array:", arr)

