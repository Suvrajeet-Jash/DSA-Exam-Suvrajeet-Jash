def rotateLeft(arr, d):
    n = len(arr)
    d = d % n   # Handle cases where d > n
    return arr[d:] + arr[:d]


#User Input

print("Enter the Elements of the Array")
lst = [int(i) for i in input().split()]

r = int(input("Enter the Number of Rotations to be done: "))
print("Original Array:", lst)
print(f"Array after {r} left rotations:", rotateLeft(lst, r))
