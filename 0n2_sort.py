# Given a list of numbers in random order, write an
# algorithm that works in O(n2) to sort the list.
# Do not use the list sort method or sorted function.

def bubble_sort(num):
    for i in range(len(num)):
        for j in range(len(num) - 1):
            if num[j] > num[j + 1]:
                num[j], num[j + 1] = num[j + 1], num[j]

numbers = [30, 16, 98, 42, 5]
print("Before sorting: ", numbers)
bubble_sort(numbers)
print("Sorted numbers: ", numbers)