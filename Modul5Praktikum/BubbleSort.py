def bubbleSort(alist):
    n = len(alist)
    for i in range (n-1):
        for j in range( n-i-1):
            if alist[j] > alist[j+1]:
                # swap 3 langkah
                # temp = alist[j]
                # alist[j] = alist[j+1]
                # alist[j+1] = temp
                # swap langsung
                alist[j], alist[j+1] = alist[j+1],alist[j]
        print("Tahap",i+1, alist)

alist = [54,26,93,17,77,31,44,55,20]
bubbleSort(alist)
print("Sorted",alist)