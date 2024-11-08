#Two lists. One with 10 strings and one with 10 ints.
unSortedFruits = ['Orange', 'Banana', 'Apple', 'Mango', 'Pear', 'Kiwi', 'Grapefruit', 'Watermelon',
           'Cranberrie', 'Avocado']

unSortedNumbers = [28, 15, 74, 12, 39, 5, 66, 50, 84, 45, 2]

# Implement a quicksort for the lists here:
#---

# Function for swaping the elements position.
def Swap(myList, i, j):
    temp = myList[i]
    myList[i] = myList[j]
    myList[j] = temp

def Part(myList, start, end):
    # The first time this function run start is 0 and the first element is picked as pivot.
    # swapIndex is 0 and end is the number of elements in the list
    pivot = myList[start]
    swapIndex = start

    i = start + 1
    while i < end:
        # If the element at index i is less than the pivot, the elements swap places
        # and the swapIndex is increased by 1 as long as i is less than the end
        if myList[i] < pivot:
            swapIndex += 1
            Swap(myList, i, swapIndex)
        i += 1

    # The pivot and the element at swapIndex can swap positions and the pivots index is returned
    Swap(myList, start, swapIndex)
    return swapIndex

# This function calls itself until the list is sorted (Runs as long as start is less than end)
def QuickSort(myList, start, end):
    if start < end:

        # Get's the pivot's index and put the lower elements compared to the pivot at a lower position and
        # higher elements at a higher positon than the pivot. 
        pivot = Part(myList, start, end)
        QuickSort(myList, start, pivot)
        QuickSort(myList, pivot + 1, end)
    return myList
    
#---

# Implement a binary search for the lists here:
#---

def BinarySearch(mySortedList, key, min, max):
    # If the max value is greater than the min value the element is not in the list
    if min > max:
        return 'Nil'
    else:
        # Divide the list in half each time until the key matches the mid value
        mid = int((min + max) / 2)

        if key == mySortedList[mid]:
            return mid
        elif key < mySortedList[mid]:
            return BinarySearch(mySortedList, key, min, mid -1)
        else:
            return BinarySearch(mySortedList, key, mid +1, max)

#---

# Prints the unsorted lists
print('Unsorted lists: ')
print(unSortedNumbers)
print(unSortedFruits)

# Copy the lists
sortedNumbers = unSortedNumbers.copy()
sortedFruits = unSortedFruits.copy()

# Wait for user to press a key to continue the program
input('Press Enter to sort the lists...')

#Sort the list copies
print('Sorted lists:')
QuickSort(sortedNumbers, 0, len(sortedNumbers))
QuickSort(sortedFruits, 0, len(sortedFruits))

# Prints the sorted lists
print(sortedNumbers)
print(sortedFruits)

# Find and stores the index of the item in the list that the user searched for
searchKey = input('Type in a fruit to search for from the list above...')
searchedFruitIndex = BinarySearch(sortedFruits, searchKey, 0, len(sortedFruits) -1)

# Prints the fruit and it's index the user serched for unless it was not in list
try:
    print('You searched for ' + sortedFruits[searchedFruitIndex] + ' at index ' + str(searchedFruitIndex) + '.')
except:
    print('Item not found in list.')

input('Press Enter to quit program...')