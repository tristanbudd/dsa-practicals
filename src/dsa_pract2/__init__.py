# Using https://www.programiz.com/dsa for info about sorting types.

"""
Question #1

Implement Selection Sort:
Recall that in each iteration, Selection Sort finds the minimum or maximum in the
unsorted part of the array and moves it to the sorted part. Repeat until the array is
fully sorted.
"""
def selection_sort(data):
    array_length = len(data)

    for i in range(array_length):
        min_index = i

        for j in range(i + 1, array_length):
            if data[j] < data[min_index]:
                min_index = j

        # Careful as need to do this at the exact same time to avoid overriding.
        data[i], data[min_index] = data[min_index], data[i]

    return data


"""
Question #2

Implement Insertion Sort:
Recall that in each iteration, Insertion Sort takes an element from the unsorted part,
finds its correct position in the sorted part, and inserts it. Repeat until the array is fully
sorted.
"""
def insertion_sort(data):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1

        while j >= 0 and key < data[j]:
            data[j + 1] = data[j]
            j = j - 1

        data[j + 1] = key

    return data


"""
Question #3

Implement Bubble Sort:
Recall that in each iteration, Bubble Sort compares adjacent elements in the unsorted
part and swaps them if needed. After each pass, the last element of the unsorted part
is in its final position. Repeat until the array is fully sorted.
"""
def bubble_sort(data):
    for i in range(len(data)):
        for j in range(0, (len(data) - i) - 1):
            if data[j] > data[j + 1]:
                data[j], data[j+1] = data[j+1], data[j]

    return data


"""
Question #4:

Implement Linear Search for an Array or List, sequentially checking each
element of the array or list to find a target value.
"""
def linear_search(data, value):
    for i in range(len(data)):
        if data[i] == value:
            return i

    return -1


"""
Question #5

Implement Binary Search for a Sorted Array (Iterative Method), halving the
search space at each step.
"""
def binary_search(data, value):
    low = 0
    high = len(data) - 1

    while low <= high:
        middle = (low + high) // 2

        # print(data[low:high+1], low, middle, high)

        if data[middle] == value:
            return middle
        elif value > data[middle]:
            low = middle + 1
        else:
            high = middle - 1

    return low


"""
Question #6

Implement Binary Search for a Sorted Array (Recursive Method) and
compare its performance with the iterative method in Ex 5 using arbitrary
sorted arrays.
"""
def binary_search_recursive(data, value, low, high):
    if high >= low:
        middle = low + (high - low) // 2

        if value == data[middle]:
            return middle
        elif value > data[middle]:
            return binary_search_recursive(data, value, middle + 1, high)
        else:
            return binary_search_recursive(data, value, low, middle - 1)
    else:
        return -1


"""
Question #7:

(Advanced) Implement Ternary Search for a Sorted Array, a method that
perform searching by dividing a sorted array into three equal parts instead of
two. Assess and compare its performance with binary search using arbitrary
sorted arrays.
"""
def ternary_search(data, value):
    pass

def main():
    print(selection_sort([64, 25, 12, 22, 11]))
    print(insertion_sort([64, 25, 12, 22, 11]))
    print(bubble_sort([64, 25, 12, 22, 11]))

    print(linear_search([11, 12, 22, 25, 64], 22))
    print(binary_search([11, 12, 22, 25, 64, 128, 256], 128))
    print(binary_search_recursive([11, 12, 22, 25, 64, 128, 256], 128, 0, 7))
    print(ternary_search([11, 12, 22, 25, 64, 128, 256], 128))

if __name__ == "__main__":
    main()