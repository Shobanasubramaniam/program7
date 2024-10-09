# Input the number of elements in the array
n = int(input("Enter the number of elements in the array: "))

# Input the array elements
arr = list(map(int, input(f"Enter {n} elements: ").split()))

# Input the element to find the last occurrence of
element = int(input("Enter the element to find: "))

# Finding the last occurrence
index = -1  # Default if the element is not found
for i in range(n):
    if arr[i] == element:
        index = i  # Update index each time the element is found

if index != -1:
    print(f"Last occurrence of {element} is at index: {index}")
else:
    print(f"{element} not found in the array.")
