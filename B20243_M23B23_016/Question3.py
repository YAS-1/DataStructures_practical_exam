
#Merge sort
#Complexity class - O(n logn)
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i=j=k=0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1

            k+=1

        while i<len(left):
            arr[k] = left[i]
            i+=1
            k+=1

        while j<len(right):
            arr[k] = right[j]
            j+=1
            k+=1



arr =[14,8,-42,11,35,-9,56,23]
merge_sort(arr)
print(arr)




#Bubble sort
#Complexity class -O(n^2)


def bubble_sort(arr):
    index = len(arr)-1
    for i in range(0,index):
        min = i
        for j in range(i+1,len(arr)):
            if arr[i] > arr[j]:
                min =j
            while min != i:
                arr[min],arr[i] = arr[i],arr[min]
    return arr                                     
     
arr =[14,8,-42,11,35,-9,56,23]
bubble_sort(arr)
print(arr)


