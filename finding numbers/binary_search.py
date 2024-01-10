#Author: Minh Nguyen
#Date: 10/27/2023
#Purpose: Performs binary search on a sorted list of random numbers.

from random import randint


# Perform binary search for key on the sublist of the_list
# starting at index left and going up to and including index right.
# If key appears in the_list, return the index where it appears.
# Otherwise, return None.
# Requires the_list to be sorted.

def binary_search(the_list, key, left = None, right = None):
    # If using the default parameters, then search the entire list.
    if left == None and right == None:
        left = 0
        right = len(the_list) - 1

    #If the sublist of the_list starting at index left and going up to and including index right
    # is empty—that is, it contains no items, not even one item—then clearly,
    # key cannot be in this sublist. Return None.
    if left > right:
        return None

    mid = (left + right) // 2 #Compute midpoint, the midpoint of this sublist, by averaging left and right.

    #If key is equal to the item at index midpoint of the_list, then it has been found. Return this index.
    if the_list[mid] == key:
        return mid
    #If key is greater than the item at the midpoint, and so if it's in the list,
    # then it must be in the sublist after the midpoint.
    # Recursively return the result of calling binary_search on the sublist
    # starting at the index just after midpoint and going up to and including index right.
    elif the_list[mid] < key:
        return binary_search(the_list, key, mid + 1, right)
    # If key is less than the item at the midpoint and it's in the list,
    # then it must be in the sublist before the midpoint.
    # Recursively return the result of calling binary_search on the sublist
    # starting at index left and going up to and including the index just before midpoint.
    elif the_list[mid] > key:
        return binary_search(the_list, key, left, mid - 1)


# Driver code for binary search.
n = int(input("How many items in the list? "))

# Make a list of n random ints.
i = 0
the_list = []
while i < n:
    the_list.append(randint(0, 1000))
    i += 1

# Binary search wants a sorted list.
the_list = sorted(the_list)
print("The list: " + str(the_list))

while True:
    key = input("What value to search for? ('?' to see the list, 'q' to quit): ")

    if key == "?":
        print("The list: " + str(the_list))
    elif key == "q":
        break
    else:
        key = int(key)
        index = binary_search(the_list, key)
        if index == None:
            print(str(key) + " not found")
        else:
            print(str(key) + " found at index " + str(index))