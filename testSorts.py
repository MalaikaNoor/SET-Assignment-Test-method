# Test Method for both BubbleSort() method and SelectionSort() method
# Created by: Malaika Noor
# Student ID: 20723989
# Purpose: For Software Engineering Testing Assignment

from sorts import *

def test_BubbleSort():
    # Test case 1: Empty array
    arr1 = []
    BubbleSort(arr1)
    assert arr1 == []

    # Test case 2: Already sorted array
    arr2 = [1, 2, 3, 4, 5]
    BubbleSort(arr2)
    assert arr2 == [1, 2, 3, 4, 5]

    # Test case 3: Array with one element
    arr3 = [5]
    BubbleSort(arr3)
    assert arr3 == [5]

    # Test case 4: Array with duplicate elements
    arr4 = [4, 3, 2, 1, 2]
    BubbleSort(arr4)
    assert arr4 == [1, 2, 2, 3, 4]

    # Test case 5: Array with negative numbers
    arr5 = [-5, -3, -2, -4, -1]
    BubbleSort(arr5)
    assert arr5 == [-5, -4, -3, -2, -1]

    # Test case 6: Random array
    arr6 = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    BubbleSort(arr6)
    assert arr6 == [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]

    print("All test cases passed successfully!")

# Call the test method
test_BubbleSort()

def test_SelectionSort():
    # Test case 1: Empty array
    arr1 = []
    SelectionSort(arr1)
    assert arr1 == []

    # Test case 2: Already sorted array
    arr2 = [1, 2, 3, 4, 5]
    SelectionSort(arr2)
    assert arr2 == [1, 2, 3, 4, 5]

    # Test case 3: Array with one element
    arr3 = [5]
    SelectionSort(arr3)
    assert arr3 == [5]

    # Test case 4: Array with duplicate elements
    arr4 = [4, 3, 2, 1, 2]
    SelectionSort(arr4)
    assert arr4 == [1, 2, 2, 3, 4]

    # Test case 5: Array with negative numbers
    arr5 = [-5, -3, -2, -4, -1]
    SelectionSort(arr5)
    assert arr5 == [-5, -4, -3, -2, -1]

    # Test case 6: Random array
    arr6 = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    SelectionSort(arr6)
    assert arr6 == [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]

    print("All test cases passed successfully!")

# Call the test method
test_SelectionSort()
