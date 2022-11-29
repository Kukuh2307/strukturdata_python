# fungsi ordered sequential search
def sequentialSearch(listData,item):
    index = 0
    found = False
    stop = False
    while index < len(listData) and not found and not stop:
        print("iterasi ke- "+ str(index+1))

        if listData[index] == item:
            found = True
        else:
            if listData[index] > item:
                stop = True
            else:
                index += 1

    if found == True:
        output = str(item) + (" Di temukan")
    else:
        output = str(item) + (" Tidak ditemukan")

    return output

# Test data dan panggil fungsi
testlist = [0,2,8,13,17,19,32,42]
print(sequentialSearch(testlist,3))
print(" ")
print(sequentialSearch(testlist,13))