# Given a list of numbers in random order,
# write insertion sort algorithm to sort the list.
# Discuss the complexity of your solution in
# terms of Big-O notation.

def insertionSort(lst):
    for indx in range(1, len(lst)):
        currentval = lst[indx]
        position = indx

        while position > 0 and lst[position-1] > currentval:
            # if item is bigger than the one before it
            # make room to insert it
            lst[position] = lst[position-1]
            position = position-1       # pushes items over so new item has space

        lst[position] = currentval      # moves current value to correct position



# in terms of big-O notation, insertion sort is O(n^2) because
# it has a nested loop. 