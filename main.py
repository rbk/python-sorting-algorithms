# Python Sorting Algorithms
import os
import sys
import time
from utilities import words, numbers_simple, numbers_complex, log
from bubble_sort import bubble_sort
from merge_sort import merge_sort

# timeit
import timeit

def main():
    os.system('clear')
    log('Python Sorting Algorithms : ' + str(time.time()))
    print("The following examples will show implementation and efficiency of various sorting algorithms.")
    log('Unsorted Arrays')
    print(words)
    print(numbers_simple)
    print(numbers_complex)
    log("Bubble Sort")
    result = bubble_sort(numbers_simple.copy())
    print('Before: ', numbers_simple)
    print('After:  ', result)
    # log("Merge Sort")
    # result = merge_sort(numbers_simple.copy())
    # print('Before: ', numbers_simple)
    # print('After:  ', result)
    log("Merge Sort Steps")
    result = merge_sort([3,2,4,1,4])
    log('Result')
    print('Before: ', [3,2,4,1,4])
    print('After:  ', result)



if __name__ == '__main__':
    main()