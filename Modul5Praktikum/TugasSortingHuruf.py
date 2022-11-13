def bubbleSort(huruf,angka):
    n = len(huruf)
    for i in range (n-1):
        for j in range( n-i-1):
            # jika ingin sorting secara desc tinggal mengubah lebih besar menjadi lebih kecil
            if huruf[j] > huruf[j+1]: 
                # swap langsung
                huruf[j], huruf[j+1] = huruf[j+1],huruf[j]
                angka[j], angka[j+1] = angka[j+1],angka[j]
        print("Tahap",i+1,huruf,"\n\t",angka)

huruf = ["w","d","b","a","z"]
angka = [7,2,0,8,4]
bubbleSort(huruf,angka)
print("Sorted",huruf,"\n\t",angka)