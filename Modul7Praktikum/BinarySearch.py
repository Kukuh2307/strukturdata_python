# fungsi Binaryl search
def BinarylSearch(testlist,item):
    count = 0
    awal = 0
    akhir = len(testlist) -1
    found = False

    while awal <= akhir and not found:
        count += 1
        print("iterasi ke-" + str(count))

        tengah = (awal + akhir)//2
        if testlist[tengah] == item:
            found = True
        else:
            if item < testlist[tengah]:
                akhir = tengah-1
            else:
                awal = tengah+1

        if found == True:
            output = str(item) + (" Di temukan")
        else:
            output = str(item) + (" Tidak ditemukan")

    return output

# Test data dan panggil fungsi
testlist = [0,1,2,8,13,17,19,32,42]
print(BinarylSearch(testlist,3))
print(" ")
print(BinarylSearch(testlist,13))