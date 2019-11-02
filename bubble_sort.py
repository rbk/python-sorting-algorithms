def bubble_sort(array):
    """Bubble Sort implemented in Python."""
    change_made = False

    for i in range(len(array)):
        # If last item 
        if i+1 != len(array):
            # print("[{} --- {}]".format(array[i], array[i+1]))
            if array[i] > array[i+1]:
                change_made = True
                array[i], array[i+1] = array[i+1], array[i]
                # print(array)

    if change_made:
        bubble_sort(array)
    else:
        return array
    return array