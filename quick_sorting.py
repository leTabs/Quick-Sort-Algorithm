# quick sorting algorithm

def quick_sort(array):
    if len(array)<=1:
        return array
        # if the array has the 1 or less items, there is nothing to be sorted
    else:
        pivot = array[0]
        # choose a certain item in the list
        # in quick sorting algorithms is usually the first or the last item
        left  = []
        right = []
        # create the arrays on wich the array get's splited into tow parts each time
        for i in range(1, len(array)):
            # looping as many times as the items in the array aside from the pivot
            if array[i] < pivot:
                left.append(array[i])
                # if the item is smaller that the pivot gets appended in the left half of the array
            else:
                right.append(array[i])
                # if not, the item gets appended in the right half of the array
        return quick_sort(left) + [pivot] + quick_sort(right)
        # the key element here is the recursion,
        # the left and right arrays don't get overwitten when rereaching the
        # lines 10 and 11 respectively

# testing...
x = [5,3,1,7,6,0,6,9,-3,3]
print(quick_sort(x))
# output: [-3, 0, 1, 3, 3, 5, 6, 6, 7, 9]
