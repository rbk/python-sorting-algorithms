


array = [100, 9, 9, 3, 1, 2, 10, 4, 6]
# array = [2, 1]

def bubble_sort(array):
    change_made = False

    new_array = []

    for i in range(len(array)):
        # print(array[i])

        # If last item 
        if i+1 != len(array):
            print("[{} --- {}]".format(array[i], array[i+1]))
            if array[i] > array[i+1]:
                change_made = True
                array[i], array[i+1] = array[i+1], array[i]
                print(array)

    if change_made:
        bubble_sort(array)
    else:
        return array
    # new_array = []

    # bubble sort
    # for i in range(len(array)):
        # print(array[i])

    # return new_array

print(bubble_sort(array))


# # Sum all numbers between a and b
# def sum(f, a, b):
#     t = 1
#     while a < b:
#         a = a + 1
#         t = t + a 
#     return t 

# print(sum("", 1, 10))