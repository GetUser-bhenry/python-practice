# Given a list of numbers in random order, write selection
# sort algorithm to sort the list. Discuss the complexity
# of your solution in terms of Big-O notation.

def selectionSort(lst):
    for fill in range (len(lst)-1, 0, -1):  # loops through all nums in list
        max = 0                             # position of max number
        for location in range(1, fill+1):
            if lst[location] > lst[max]:    # finding index of max
                max = location
        lst[fill], lst[max] = lst[max], lst[fill] #swapping items


numbers = [78, 123, 90, 3, 14, 65]
selectionSort(numbers)
print(numbers)

# in terms of big-O notation, the selection sort algorithm is
# O(n^2) because of the two nested loops.