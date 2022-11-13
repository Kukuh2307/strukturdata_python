def selectionSort(alist):
    n = len(alist)
    for i in range (n-1):
        currenminimum = i
        for j in range (i+1, n):
            # jika ingin sorting secara desc tinggal mengubah lebih besar menjadi lebih kecil
            if alist[j] < alist[currenminimum]:
                currenminimum = j
        alist[i], alist[currenminimum] = alist[currenminimum], alist[i]
        print("Tahap",i+1, alist)

alist = [54,26,93,17,77,31,44,55,20]
selectionSort(alist)
print("Sorted",alist)