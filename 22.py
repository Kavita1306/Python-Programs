arr = [32,95,57,18,23,29,654]

def bubble_sort(arr):
    n = len(arr)
    for i in range(0,n):
        for j in range(0,n-i-1):
            if (arr[j] > arr[j+1]):
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    return arr
bubble_sort(arr)
print(arr)
print("3rd smallest number from list is "+str(arr[2]))
