def insertionSort(alist):
    for index in range (1,len(alist)):
        currentvalue = alist[index]
        position = index

        # jika ingin mengurutkan secara desc tinggal mengubah tanda lebih besar menjadi lebih kecil
        while position > 0 and alist[position-1]>currentvalue:
            alist[position]=alist[position-1]
            position = position-1
        
        alist[position]=currentvalue
        print("Insertion Index",index+1,alist)

alist = [54,26,93,17,77,31,44,55,20]
insertionSort(alist)
print("Sorted",alist)