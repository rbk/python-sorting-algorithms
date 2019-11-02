def merge_sort(array):
    if len(array) > 1:
        half = int(len(array)/2)
        # print('SPLIT ', half)
        left = array[:half]
        right = array[half:]
        
        print(left, " - ",right)
        merge_sort(left)
        merge_sort(right)


        i = 0
        j = 0
        k = 0
        
        while i < len(right) and j < len(left):
            # print("{} - {}".format(left[j], right[i]))
            if right[i] < left[j]:
                array[k] = right[i]
                i+=1
            else:
                array[k] = left[j]
                j+=1
            k += 1

        # i = 0
        # while i < len(left): 
        #     array[k] = left[j] 
        #     j+=1
        #     k+=1
        
        # j = 0
        # while j < len(right): 
        #     array[k] = right[i] 
        #     i+=1
        #     k+=1

    return array
